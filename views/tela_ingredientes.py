"""
tela_ingredientes.py — Lista de pratos à esquerda; ingredientes do prato
selecionado exibidos à direita.
"""

import customtkinter as ctk
from views import BaseTela
from utils.helpers import load_json, AppState


class TelaIngredientes(BaseTela):

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, state, navigate, title="Ingredientes", icon="📋")
        self._plano = load_json("plano_alimentar.json")
        self._receitas = load_json("receitas_fds.json")
        self._items: list[dict] = []   # {"label": str, "ingredientes": list[str]}
        self._build_items_index()
        self._build_content()

    # ── Índice de itens seleccionáveis ─────────────────────────────────────────
    def _build_items_index(self) -> None:
        for ref in self._plano.get("refeicoes", []):
            for v in ref.get("variacoes_de_pratos", []):
                self._items.append({
                    "label": f"{ref['horario']} — {v['nome']}",
                    "ingredientes": v.get("ingredientes_principais", []),
                })
        for r in self._receitas.get("receitas", []):
            self._items.append({
                "label": f"🍳 {r['nome']}",
                "ingredientes": r.get("ingredientes", []),
            })

    # ── Conteúdo ───────────────────────────────────────────────────────────────
    def _build_content(self) -> None:
        body = ctk.CTkFrame(self, corner_radius=0)
        body.pack(fill="both", expand=True, padx=16, pady=(8, 16))
        body.grid_columnconfigure(0, weight=1, minsize=340)
        body.grid_columnconfigure(1, weight=2)
        body.grid_rowconfigure(0, weight=1)

        # Painel esquerdo — lista de pratos
        left = ctk.CTkFrame(body, corner_radius=10)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=0)

        ctk.CTkLabel(
            left, text="Selecione um prato:", font=self.state.f("subheading"),
        ).pack(padx=12, pady=(12, 6))

        list_frame = ctk.CTkScrollableFrame(left)
        list_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self._selected_btn = None
        for item in self._items:
            btn = ctk.CTkButton(
                list_frame,
                text=item["label"],
                font=self.state.f("body"),
                anchor="w",
                height=46,
                fg_color="transparent",
                text_color=("black", "white"),
                hover_color=("gray80", "gray35"),
                command=lambda it=item: self._show_ingredients(it),
            )
            btn.pack(fill="x", padx=4, pady=3)

        # Painel direito — ingredientes
        self._right = ctk.CTkFrame(body, corner_radius=10)
        self._right.grid(row=0, column=1, sticky="nsew", padx=(0, 0), pady=0)

        self._right_label = ctk.CTkLabel(
            self._right,
            text="← Selecione um prato na lista",
            font=self.state.f("body"),
            text_color="gray",
        )
        self._right_label.pack(expand=True)

    def _show_ingredients(self, item: dict) -> None:
        # Limpa painel direito
        for w in self._right.winfo_children():
            w.destroy()

        ctk.CTkLabel(
            self._right,
            text=item["label"],
            font=self.state.f("subheading"),
            anchor="w",
            wraplength=700,
        ).pack(fill="x", padx=16, pady=(14, 6))

        ctk.CTkLabel(
            self._right,
            text="Ingredientes:",
            font=self.state.f("body"),
            anchor="w",
            text_color=("gray40", "gray70"),
        ).pack(fill="x", padx=16, pady=(0, 4))

        scroll = ctk.CTkScrollableFrame(self._right)
        scroll.pack(fill="both", expand=True, padx=10, pady=(0, 12))

        ings = item.get("ingredientes", [])
        if not ings:
            ctk.CTkLabel(
                scroll,
                text="(Ingredientes não disponíveis para este item)",
                font=self.state.f("body"),
                text_color="gray",
            ).pack(padx=12, pady=10)
        else:
            for i, ing in enumerate(ings, 1):
                row = ctk.CTkFrame(scroll, corner_radius=8, fg_color=("gray92", "gray25"))
                row.pack(fill="x", padx=6, pady=4)
                ctk.CTkLabel(
                    row,
                    text=f"  {i:>2}.  {ing}",
                    font=self.state.f("body"),
                    anchor="w",
                ).pack(fill="x", padx=12, pady=10)
