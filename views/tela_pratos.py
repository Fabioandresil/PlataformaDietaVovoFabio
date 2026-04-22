"""
tela_pratos.py — Exibe as refeições do dia em abas e as receitas de fim de semana.
Cada aba mostra os pratos sugeridos como cards clicáveis.
"""

import customtkinter as ctk
from views import BaseTela
from utils.helpers import load_json, AppState


class TelaPratos(BaseTela):

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, state, navigate, title="Pratos Sugeridos", icon="🍽️")
        self._plano = load_json("plano_alimentar.json")
        self._receitas = load_json("receitas_fds.json")
        self._build_content()

    # ── Conteúdo ───────────────────────────────────────────────────────────────
    def _build_content(self) -> None:
        tabs = ctk.CTkTabview(self, height=680)
        tabs.pack(fill="both", expand=True, padx=16, pady=(8, 16))

        # Abas por refeição
        for ref in self._plano.get("refeicoes", []):
            horario = ref.get("horario", "")
            nome = ref.get("nome", "")
            label = f"{horario} — {nome}"
            tabs.add(label)
            self._populate_refeicao_tab(tabs.tab(label), ref)

        # Aba receitas de fim de semana
        tabs.add("📅 Receitas FDS")
        self._populate_receitas_tab(tabs.tab("📅 Receitas FDS"))

    def _populate_refeicao_tab(self, tab, ref: dict) -> None:
        # Scroll horizontal via frame
        scroll = ctk.CTkScrollableFrame(tab, orientation="vertical")
        scroll.pack(fill="both", expand=True, padx=8, pady=8)

        variacoes = ref.get("variacoes_de_pratos", [])
        horario = ref.get("horario", "")

        for v in variacoes:
            self._card(scroll, v["nome"], v["descricao"], horario)

        # Notas da refeição
        notas = ref.get("notas", [])
        if notas:
            ctk.CTkLabel(
                scroll,
                text="📌 Notas:",
                font=self.state.f("subheading"),
                anchor="w",
            ).pack(fill="x", padx=10, pady=(18, 2))
            for nota in notas:
                ctk.CTkLabel(
                    scroll,
                    text=f"  • {nota}",
                    font=self.state.f("body"),
                    anchor="w",
                    wraplength=900,
                    justify="left",
                ).pack(fill="x", padx=20, pady=2)

    def _populate_receitas_tab(self, tab) -> None:
        scroll = ctk.CTkScrollableFrame(tab, orientation="vertical")
        scroll.pack(fill="both", expand=True, padx=8, pady=8)

        for receita in self._receitas.get("receitas", []):
            self._card(
                scroll,
                receita["nome"],
                f"Tipo: {receita.get('tipo', '')}  •  {len(receita.get('ingredientes', []))} ingredientes",
                "Fim de semana",
                color="#004D40",
            )

    def _card(
        self,
        parent,
        titulo: str,
        descricao: str,
        horario: str,
        color: str = "#1565C0",
    ) -> None:
        card = ctk.CTkFrame(parent, corner_radius=12, fg_color=("gray93", "gray22"))
        card.pack(fill="x", padx=10, pady=8)

        inner = ctk.CTkFrame(card, corner_radius=10, fg_color=color)
        inner.pack(fill="x", padx=3, pady=3)

        ctk.CTkLabel(
            inner,
            text=titulo,
            font=self.state.f("subheading"),
            text_color="white",
            anchor="w",
        ).pack(fill="x", padx=16, pady=(10, 2))

        ctk.CTkLabel(
            inner,
            text=descricao,
            font=self.state.f("body"),
            text_color="white",
            anchor="w",
            wraplength=900,
            justify="left",
        ).pack(fill="x", padx=16, pady=(2, 4))

        ctk.CTkLabel(
            inner,
            text=f"🕐 {horario}",
            font=self.state.f("small"),
            text_color="#BBDEFB",
            anchor="w",
        ).pack(fill="x", padx=16, pady=(0, 10))
