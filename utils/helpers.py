"""
helpers.py — Funções auxiliares: carregamento de dados, estado da aplicação,
timer de hidratação e persistência de preferências.
"""

import os
import json
from datetime import date

try:
    import customtkinter as ctk
    CTK_AVAILABLE = True
except ImportError:
    CTK_AVAILABLE = False

# ── Caminhos base ──────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
PREFS_FILE = os.path.join(BASE_DIR, "preferences.json")


# ── Carregamento de dados ──────────────────────────────────────────────────────
def load_json(filename: str) -> dict:
    """Carrega um arquivo JSON da pasta data/ com tratamento de erros."""
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[AVISO] Arquivo não encontrado: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERRO] JSON inválido em {path}: {e}")
        return {}


def load_preferences() -> dict:
    """Carrega preferências do usuário de preferences.json."""
    try:
        with open(PREFS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "dark_mode": False,
            "font_delta": 0,
            "hydration_cups": 0,
            "hydration_date": str(date.today()),
            "red_meat_days": [],
            "red_meat_week": "",
        }


def save_preferences(prefs: dict) -> None:
    """Salva preferências do usuário em preferences.json."""
    try:
        with open(PREFS_FILE, "w", encoding="utf-8") as f:
            json.dump(prefs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERRO] Não foi possível salvar preferências: {e}")


# ── Categorização de ingredientes ─────────────────────────────────────────────
CATEGORIAS = {
    "🍎 Frutas": [
        "mamão", "manga", "ameixa", "pera", "maçã", "banana", "limão",
        "laranja", "melão", "melancia", "abacate", "goiaba", "caju",
    ],
    "🥩 Proteínas": [
        "ovo", "frango", "peixe", "carne", "atum", "ricota", "peito",
        "carne moída", "frango moído",
    ],
    "🧀 Laticínios": [
        "leite", "queijo minas", "queijo", "iogurte",
    ],
    "🥦 Legumes / Verduras": [
        "abobrinha", "cenoura", "brócolis", "alface", "rúcula", "tomate",
        "pepino", "rabanete", "acelga", "repolho", "cebola", "alho",
        "inhame", "berinjela", "couve", "couve-flor", "salsinha", "cebolinha",
        "salsa",
    ],
    "🌾 Carboidratos": [
        "arroz", "mandioca", "pão", "cuscuz", "aveia", "tapioca", "trigo",
        "biscoito", "torrada", "farinha", "farelo", "grão de bico",
        "macarrão", "tapioca", "batata",
    ],
    "🌰 Sementes / Fibras": [
        "linhaça", "chia", "psyllium", "semente", "girassol",
    ],
    "🫘 Leguminosas": [
        "feijão", "lentilha", "ervilha seca", "grão de bico",
    ],
    "🌿 Temperos / Condimentos": [
        "azeite", "sal", "pimenta", "orégano", "salsinha", "cebolinha",
        "gengibre", "manjericão", "alecrim", "coentro", "páprica",
        "noz moscada", "ervas", "tempero", "limão",
    ],
}


def categorize_ingredient(text: str) -> str:
    """Retorna a categoria de um ingrediente baseado em palavras-chave."""
    t = text.lower()
    for categoria, palavras in CATEGORIAS.items():
        if any(p in t for p in palavras):
            return categoria
    return "📦 Outros"


def consolidate_ingredients(ingredient_lists: list[list[str]]) -> dict[str, list[str]]:
    """
    Recebe uma lista de listas de ingredientes (strings) e retorna um dicionário
    agrupado por categoria, com ingredientes únicos (normalizados).
    """
    seen = set()
    categorized: dict[str, list[str]] = {}

    for ing_list in ingredient_lists:
        for ing in ing_list:
            key = ing.strip().lower()
            if key and key not in seen:
                seen.add(key)
                cat = categorize_ingredient(ing)
                categorized.setdefault(cat, []).append(ing.strip())

    return categorized


# ── Estado global da aplicação ────────────────────────────────────────────────
class AppState:
    """Gerencia fontes, tema, hidratação e preferências globais."""

    _BASE_SIZES = {
        "title":      28,
        "heading":    24,
        "subheading": 20,
        "body":       18,
        "small":      16,
        "button":     20,
        "alert":      22,
        "mono":       16,
    }

    def __init__(self, prefs: dict | None = None):
        self.prefs = prefs or {}
        self.dark_mode: bool = self.prefs.get("dark_mode", False)
        self.font_delta: int = self.prefs.get("font_delta", 0)
        self.navigator = None
        self.hydration_timer: "HydrationTimer | None" = None

        # Hidratação — reseta diariamente
        today = str(date.today())
        if self.prefs.get("hydration_date") != today:
            self.hydration_cups = 0
        else:
            self.hydration_cups = self.prefs.get("hydration_cups", 0)

        # Carne vermelha — reseta semanalmente
        from datetime import datetime
        current_week = datetime.now().strftime("%Y-W%W")
        if self.prefs.get("red_meat_week") != current_week:
            self.red_meat_days: set = set()
        else:
            self.red_meat_days = set(self.prefs.get("red_meat_days", []))

        self._cup_callbacks: list = []

        # Fontes CTk (criadas após inicialização do CTk)
        if CTK_AVAILABLE:
            self._init_ctk_fonts()

    def _init_ctk_fonts(self) -> None:
        d = self.font_delta
        self.fonts = {
            name: ctk.CTkFont(
                size=size + d,
                weight="bold" if name in ("title", "heading", "subheading", "button", "alert") else "normal",
            )
            for name, size in self._BASE_SIZES.items()
        }

    def f(self, role: str):
        """Retorna o CTkFont para o papel indicado."""
        if CTK_AVAILABLE and hasattr(self, "fonts"):
            return self.fonts.get(role, self.fonts["body"])
        return None

    # ── Fonte ──────────────────────────────────────────────────────────────────
    def increase_font(self) -> None:
        if self.font_delta < 10:
            self.font_delta += 2
            self._apply_font_delta(+2)

    def decrease_font(self) -> None:
        if self.font_delta > -4:
            self.font_delta -= 2
            self._apply_font_delta(-2)

    def _apply_font_delta(self, diff: int) -> None:
        if CTK_AVAILABLE and hasattr(self, "fonts"):
            for font in self.fonts.values():
                current = font.cget("size")
                font.configure(size=max(12, current + diff))

    # ── Tema ───────────────────────────────────────────────────────────────────
    def toggle_theme(self) -> None:
        self.dark_mode = not self.dark_mode
        if CTK_AVAILABLE:
            ctk.set_appearance_mode("dark" if self.dark_mode else "light")

    # ── Hidratação ─────────────────────────────────────────────────────────────
    def add_cup(self) -> None:
        self.hydration_cups += 1
        for cb in self._cup_callbacks:
            try:
                cb(self.hydration_cups)
            except Exception:
                pass

    def register_cup_callback(self, cb) -> None:
        self._cup_callbacks.append(cb)

    # ── Preferências ───────────────────────────────────────────────────────────
    def get_preferences(self) -> dict:
        from datetime import datetime
        return {
            "dark_mode": self.dark_mode,
            "font_delta": self.font_delta,
            "hydration_cups": self.hydration_cups,
            "hydration_date": str(date.today()),
            "red_meat_days": list(self.red_meat_days),
            "red_meat_week": datetime.now().strftime("%Y-W%W"),
        }


# ── Timer de hidratação ────────────────────────────────────────────────────────
class HydrationTimer:
    """
    Timer baseado em tkinter.after() que conta regressivamente 60 minutos.
    Exibe popup e chama callbacks registrados a cada segundo.
    """

    INTERVAL_SECONDS = 3600  # 1 hora

    def __init__(self, root, state: AppState):
        self.root = root
        self.state = state
        self._running = False
        self._countdown = self.INTERVAL_SECONDS
        self._display_callbacks: list = []

    def start(self) -> None:
        self._running = True
        self._tick()

    def stop(self) -> None:
        self._running = False

    def reset(self) -> None:
        self._countdown = self.INTERVAL_SECONDS

    def register_display_callback(self, cb) -> None:
        """Registra callback que recebe a string de contagem regressiva (MM:SS)."""
        self._display_callbacks.append(cb)

    def get_countdown_str(self) -> str:
        m = self._countdown // 60
        s = self._countdown % 60
        return f"{m:02d}:{s:02d}"

    def _tick(self) -> None:
        if not self._running:
            return
        self._countdown -= 1
        if self._countdown <= 0:
            self._countdown = self.INTERVAL_SECONDS
            self._show_popup()

        txt = self.get_countdown_str()
        for cb in self._display_callbacks:
            try:
                cb(txt)
            except Exception:
                pass

        self.root.after(1000, self._tick)

    def _show_popup(self) -> None:
        try:
            if CTK_AVAILABLE:
                popup = ctk.CTkToplevel(self.root)
                popup.title("💧 Hora de Beber Água!")
                popup.geometry("480x240")
                popup.resizable(False, False)
                popup.grab_set()
                popup.lift()
                popup.focus_force()

                ctk.CTkLabel(
                    popup,
                    text="💧  Hora de Beber Água!",
                    font=ctk.CTkFont(size=26, weight="bold"),
                    text_color="#2196F3",
                ).pack(pady=(25, 5))

                ctk.CTkLabel(
                    popup,
                    text="Tome um copo de água agora.\nMeta diária: 8 copos (2 litros)",
                    font=ctk.CTkFont(size=18),
                ).pack(pady=8)

                def marcar_e_fechar():
                    self.state.add_cup()
                    popup.destroy()

                ctk.CTkButton(
                    popup,
                    text="✅  Bebi meu copo!",
                    font=ctk.CTkFont(size=18, weight="bold"),
                    height=52,
                    width=220,
                    fg_color="#2196F3",
                    command=marcar_e_fechar,
                ).pack(pady=12)

                ctk.CTkButton(
                    popup,
                    text="Lembrar depois",
                    font=ctk.CTkFont(size=15),
                    height=36,
                    fg_color="gray",
                    command=popup.destroy,
                ).pack()
            else:
                import tkinter.messagebox as mb
                mb.showinfo(
                    "💧 Hora de Beber Água!",
                    "Tome um copo de água agora!\nMeta: 2 litros por dia",
                )
        except Exception as e:
            print(f"[TIMER] Erro ao exibir popup: {e}")
