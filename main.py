"""
main.py — Ponto de entrada da Plataforma de Dieta — Vovô Fabio.

Uso:
    python main.py
"""

import sys
import os

# Garante que o diretório raiz do projeto esteja no sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import customtkinter as ctk
    CTK_AVAILABLE = True
except ImportError:
    import tkinter as tk
    CTK_AVAILABLE = False
    print("[AVISO] CustomTkinter não instalado. Execute: pip install customtkinter")

from utils.helpers import AppState, HydrationTimer, load_preferences, save_preferences


class AppManager:
    """Gerencia todas as telas e a navegação entre elas."""

    def __init__(self, root, state: AppState):
        self.root = root
        self.state = state
        state.navigator = self

        if CTK_AVAILABLE:
            self.container = ctk.CTkFrame(root, corner_radius=0)
        else:
            import tkinter as tk
            self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.frames: dict = {}
        self._load_frames()
        self.navigate("principal")

    def _load_frames(self) -> None:
        from views.tela_principal import TelaPrincipal
        from views.tela_pratos import TelaPratos
        from views.tela_ingredientes import TelaIngredientes
        from views.tela_preparo import TelaPreparo
        from views.tela_lista_supermercado import TelaListaSupermercado
        from views.tela_dieta_completa import TelaDietaCompleta
        from views.tela_recomendacoes import TelaRecomendacoes

        telas = {
            "principal":        TelaPrincipal,
            "pratos":           TelaPratos,
            "ingredientes":     TelaIngredientes,
            "preparo":          TelaPreparo,
            "lista_supermercado": TelaListaSupermercado,
            "dieta_completa":   TelaDietaCompleta,
            "recomendacoes":    TelaRecomendacoes,
        }

        for name, Cls in telas.items():
            frame = Cls(self.container, self.state, self.navigate)
            self.frames[name] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def navigate(self, screen: str) -> None:
        frame = self.frames.get(screen)
        if frame:
            frame.lift()
            if hasattr(frame, "on_show"):
                frame.on_show()


def on_close(root, state: AppState) -> None:
    save_preferences(state.get_preferences())
    if state.hydration_timer:
        state.hydration_timer.stop()
    root.destroy()


def main() -> None:
    prefs = load_preferences()

    if CTK_AVAILABLE:
        mode = "dark" if prefs.get("dark_mode", False) else "light"
        ctk.set_appearance_mode(mode)
        ctk.set_default_color_theme("blue")
        root = ctk.CTk()
    else:
        import tkinter as tk
        root = tk.Tk()

    root.title("🍽️ Plataforma de Dieta — Vovô Fabio")
    root.geometry("1300x840")
    root.minsize(1000, 680)

    # Centralizar janela na tela
    root.update_idletasks()
    w, h = 1300, 840
    x = (root.winfo_screenwidth() - w) // 2
    y = (root.winfo_screenheight() - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")

    state = AppState(prefs)

    app = AppManager(root, state)

    # Timer de hidratação
    timer = HydrationTimer(root, state)
    timer.start()
    state.hydration_timer = timer

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, state))
    root.mainloop()


if __name__ == "__main__":
    main()
