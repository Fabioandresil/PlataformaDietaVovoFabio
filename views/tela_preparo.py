"""
tela_preparo.py — Lista de pratos à esquerda; modo de preparo passo a passo
exibido à direita. Botões A+ / A− ajustam a fonte do preparo.
"""

import customtkinter as ctk
from views import BaseTela
from utils.helpers import load_json, AppState


class TelaPreparo(BaseTela):

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, state, navigate, title="Forma de Preparo", icon="👨‍🍳")
        self._plano = load_json("plano_alimentar.json")
        self._receitas = load_json("receitas_fds.json")
        self._items: list[dict] = []
        self._build_items_index()
        self._build_content()

    # ── Índice ─────────────────────────────────────────────────────────────────
    def _build_items_index(self) -> None:
        # Receitas de fim de semana têm modo_preparo completo
        for r in self._receitas.get("receitas", []):
            self._items.append({
                "label": f"🍳 {r['nome']}  ({r.get('tipo', '')})",
                "nome": r["nome"],
                "passos": r.get("modo_preparo", []),
                "tipo": "receita",
            })
        # Variações do plano alimentar têm notas gerais da refeição
        for ref in self._plano.get("refeicoes", []):
            notas = ref.get("notas", [])
            if notas:
                for v in ref.get("variacoes_de_pratos", []):
                    self._items.append({
                        "label": f"{ref['horario']} — {v['nome']}",
                        "nome": v["nome"],
                        "passos": notas,
                        "tipo": "nota",
                        "horario": ref["horario"],
                    })

    # ── Conteúdo ───────────────────────────────────────────────────────────────
    def _build_content(self) -> None:
        body = ctk.CTkFrame(self, corner_radius=0)
        body.pack(fill="both", expand=True, padx=16, pady=(8, 16))
        body.grid_columnconfigure(0, weight=1, minsize=340)
        body.grid_columnconfigure(1, weight=2)
        body.grid_rowconfigure(0, weight=1)

        # Painel esquerdo
        left = ctk.CTkFrame(body, corner_radius=10)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        ctk.CTkLabel(
            left, text="Selecione um prato:", font=self.state.f("subheading"),
        ).pack(padx=12, pady=(12, 6))

        list_scroll = ctk.CTkScrollableFrame(left)
        list_scroll.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        for item in self._items:
            ctk.CTkButton(
                list_scroll,
                text=item["label"],
                font=self.state.f("body"),
                anchor="w",
                height=46,
                fg_color="transparent",
                text_color=("black", "white"),
                hover_color=("gray80", "gray35"),
                command=lambda it=item: self._show_preparo(it),
            ).pack(fill="x", padx=4, pady=3)

        # Painel direito
        self._right = ctk.CTkFrame(body, corner_radius=10)
        self._right.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(
            self._right,
            text="← Selecione um prato na lista",
            font=self.state.f("body"),
            text_color="gray",
        ).pack(expand=True)

    # ── Exibir preparo ────────────────────────────────────────────────────────
    def _show_preparo(self, item: dict) -> None:
        for w in self._right.winfo_children():
            w.destroy()

        # Barra superior com título + A+/A−
        topbar = ctk.CTkFrame(self._right, corner_radius=0, fg_color="transparent")
        topbar.pack(fill="x", padx=12, pady=(12, 4))

        ctk.CTkLabel(
            topbar,
            text=item["nome"],
            font=self.state.f("subheading"),
            anchor="w",
            wraplength=640,
        ).pack(side="left", fill="x", expand=True)

        ctk.CTkButton(
            topbar, text="A−", width=50, height=36,
            font=self.state.f("body"),
            fg_color=("gray65", "gray40"),
            command=self.state.decrease_font,
        ).pack(side="right", padx=2)
        ctk.CTkButton(
            topbar, text="A+", width=50, height=36,
            font=self.state.f("body"),
            fg_color=("gray65", "gray40"),
            command=self.state.increase_font,
        ).pack(side="right", padx=(0, 2))

        if item["tipo"] == "nota":
            ctk.CTkLabel(
                self._right,
                text="📌 Orientações gerais para esta refeição:",
                font=self.state.f("body"),
                anchor="w",
                text_color=("gray40", "gray70"),
            ).pack(fill="x", padx=16, pady=(0, 4))
        else:
            total = len(item["passos"])
            ctk.CTkLabel(
                self._right,
                text=f"Modo de Preparo — {total} passo{'s' if total > 1 else ''}:",
                font=self.state.f("body"),
                anchor="w",
                text_color=("gray40", "gray70"),
            ).pack(fill="x", padx=16, pady=(0, 4))

        scroll = ctk.CTkScrollableFrame(self._right)
        scroll.pack(fill="both", expand=True, padx=10, pady=(0, 12))

        for i, passo in enumerate(item["passos"], 1):
            row = ctk.CTkFrame(scroll, corner_radius=10, fg_color=("gray92", "gray25"))
            row.pack(fill="x", padx=6, pady=5)

            lbl_num = ctk.CTkLabel(
                row,
                text=f"Passo {i}",
                font=self.state.f("small"),
                text_color=("gray45", "gray65"),
                anchor="nw",
                width=70,
            )
            lbl_num.pack(side="left", padx=(14, 4), pady=12, anchor="nw")

            ctk.CTkLabel(
                row,
                text=passo,
                font=self.state.f("body"),
                anchor="nw",
                justify="left",
                wraplength=580,
            ).pack(side="left", padx=4, pady=12, fill="x", expand=True)
