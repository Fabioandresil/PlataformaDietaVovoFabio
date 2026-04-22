"""
tela_lista_supermercado.py — Checkboxes de pratos à esquerda;
lista consolidada por categoria à direita. Botões Copiar, Imprimir e Limpar.
"""

import tkinter as tk
import customtkinter as ctk
from views import BaseTela
from utils.helpers import load_json, AppState, consolidate_ingredients


class TelaListaSupermercado(BaseTela):

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, state, navigate, title="Lista de Supermercado", icon="🛒")
        self._plano = load_json("plano_alimentar.json")
        self._receitas = load_json("receitas_fds.json")
        self._all_pratos: list[dict] = []  # {"label", "ingredientes", "var"}
        self._checkboxes: list[tuple[tk.BooleanVar, dict]] = []
        self._build_pratos_index()
        self._build_content()

    # ── Índice de pratos ───────────────────────────────────────────────────────
    def _build_pratos_index(self) -> None:
        for ref in self._plano.get("refeicoes", []):
            for v in ref.get("variacoes_de_pratos", []):
                self._all_pratos.append({
                    "label": f"{ref['horario']} — {v['nome']}",
                    "group": f"{ref['horario']} {ref['nome']}",
                    "ingredientes": v.get("ingredientes_principais", []),
                })
        for r in self._receitas.get("receitas", []):
            self._all_pratos.append({
                "label": f"🍳 {r['nome']}",
                "group": "Receitas Fins de Semana",
                "ingredientes": r.get("ingredientes", []),
            })

    # ── Conteúdo ───────────────────────────────────────────────────────────────
    def _build_content(self) -> None:
        body = ctk.CTkFrame(self, corner_radius=0)
        body.pack(fill="both", expand=True, padx=16, pady=(8, 16))
        body.grid_columnconfigure(0, weight=1, minsize=380)
        body.grid_columnconfigure(1, weight=2)
        body.grid_rowconfigure(0, weight=1)

        # ── Painel esquerdo — checkboxes ───────────────────────────────────────
        left = ctk.CTkFrame(body, corner_radius=10)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        ctk.CTkLabel(
            left, text="Escolher Pratos da Semana:",
            font=self.state.f("subheading"),
        ).pack(padx=12, pady=(12, 4))

        left_scroll = ctk.CTkScrollableFrame(left)
        left_scroll.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        current_group = None
        for prato in self._all_pratos:
            if prato["group"] != current_group:
                current_group = prato["group"]
                ctk.CTkLabel(
                    left_scroll,
                    text=current_group,
                    font=self.state.f("small"),
                    text_color=("gray40", "gray70"),
                    anchor="w",
                ).pack(fill="x", padx=8, pady=(10, 2))

            var = tk.BooleanVar(value=False)
            cb = ctk.CTkCheckBox(
                left_scroll,
                text=prato["label"],
                variable=var,
                font=self.state.f("body"),
                checkbox_width=26,
                checkbox_height=26,
                command=self._update_list,
            )
            cb.pack(anchor="w", padx=12, pady=4)
            self._checkboxes.append((var, prato))

        # Botão limpar seleção
        ctk.CTkButton(
            left,
            text="🔄 Limpar Seleção",
            font=self.state.f("body"),
            height=44,
            fg_color=("gray65", "gray40"),
            command=self._clear_selection,
        ).pack(fill="x", padx=12, pady=(4, 12))

        # ── Painel direito — lista de compras ──────────────────────────────────
        right = ctk.CTkFrame(body, corner_radius=10)
        right.grid(row=0, column=1, sticky="nsew")

        right_header = ctk.CTkFrame(right, corner_radius=0, fg_color="transparent")
        right_header.pack(fill="x", padx=12, pady=(12, 4))

        ctk.CTkLabel(
            right_header, text="Sua Lista de Compras:",
            font=self.state.f("subheading"),
        ).pack(side="left")

        ctk.CTkButton(
            right_header, text="🖨️ Imprimir / Salvar",
            font=self.state.f("small"), width=160, height=38,
            command=self._save_list,
        ).pack(side="right", padx=4)

        ctk.CTkButton(
            right_header, text="📋 Copiar",
            font=self.state.f("small"), width=110, height=38,
            command=self._copy_list,
        ).pack(side="right", padx=4)

        self._list_scroll = ctk.CTkScrollableFrame(right)
        self._list_scroll.pack(fill="both", expand=True, padx=8, pady=(0, 12))

        self._empty_label = ctk.CTkLabel(
            self._list_scroll,
            text="← Marque pratos para gerar a lista",
            font=self.state.f("body"),
            text_color="gray",
        )
        self._empty_label.pack(expand=True, pady=40)

    # ── Atualização da lista ───────────────────────────────────────────────────
    def _update_list(self) -> None:
        selected_ings = [
            prato["ingredientes"]
            for var, prato in self._checkboxes
            if var.get()
        ]

        for w in self._list_scroll.winfo_children():
            w.destroy()

        if not selected_ings:
            ctk.CTkLabel(
                self._list_scroll,
                text="← Marque pratos para gerar a lista",
                font=self.state.f("body"),
                text_color="gray",
            ).pack(expand=True, pady=40)
            return

        categorized = consolidate_ingredients(selected_ings)

        for categoria, items in sorted(categorized.items()):
            ctk.CTkLabel(
                self._list_scroll,
                text=categoria,
                font=self.state.f("subheading"),
                anchor="w",
                fg_color=("gray88", "gray22"),
                corner_radius=6,
            ).pack(fill="x", padx=6, pady=(10, 2))

            for ing in items:
                ctk.CTkLabel(
                    self._list_scroll,
                    text=f"   ☐  {ing}",
                    font=self.state.f("body"),
                    anchor="w",
                    justify="left",
                    wraplength=560,
                ).pack(fill="x", padx=20, pady=3)

    # ── Acções ────────────────────────────────────────────────────────────────
    def _clear_selection(self) -> None:
        for var, _ in self._checkboxes:
            var.set(False)
        self._update_list()

    def _get_list_text(self) -> str:
        selected_ings = [
            p["ingredientes"] for v, p in self._checkboxes if v.get()
        ]
        if not selected_ings:
            return "Nenhum prato selecionado."

        categorized = consolidate_ingredients(selected_ings)
        lines = ["=== LISTA DE COMPRAS — VOVÔ FABIO ===\n"]
        for cat, items in sorted(categorized.items()):
            lines.append(f"\n{cat}")
            lines.append("─" * 40)
            for ing in items:
                lines.append(f"  ☐  {ing}")
        return "\n".join(lines)

    def _copy_list(self) -> None:
        txt = self._get_list_text()
        self.clipboard_clear()
        self.clipboard_append(txt)
        ctk.CTkToplevel._default_appearance_mode = ctk.get_appearance_mode()
        self._show_toast("✅ Lista copiada para a área de transferência!")

    def _save_list(self) -> None:
        import os
        txt = self._get_list_text()
        path = os.path.join(
            os.path.expanduser("~"), "Desktop", "lista_supermercado_vovoFabio.txt"
        )
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(txt)
            self._show_toast(f"✅ Arquivo salvo na Área de Trabalho:\n{os.path.basename(path)}")
        except Exception as e:
            self._show_toast(f"❌ Erro ao salvar: {e}")

    def _show_toast(self, msg: str) -> None:
        popup = ctk.CTkToplevel(self)
        popup.title("Aviso")
        popup.geometry("480x160")
        popup.resizable(False, False)
        popup.grab_set()
        popup.lift()
        ctk.CTkLabel(
            popup, text=msg, font=self.state.f("body"), wraplength=440,
        ).pack(expand=True, pady=20, padx=20)
        ctk.CTkButton(
            popup, text="OK", font=self.state.f("body"), width=100, height=42,
            command=popup.destroy,
        ).pack(pady=(0, 16))
