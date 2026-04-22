"""
tela_principal.py — Tela inicial com os 6 botões de navegação e rodapé
de hidratação com contagem regressiva.
"""

import customtkinter as ctk
from utils.helpers import AppState


class TelaPrincipal(ctk.CTkFrame):

    BOTOES = [
        ("🍽️", "PRATOS\nSUGERIDOS",          "pratos",            "#1565C0", "#0D47A1"),
        ("📋", "INGREDIENTES",                 "ingredientes",      "#2E7D32", "#1B5E20"),
        ("👨‍🍳", "FORMA DE\nPREPARO",           "preparo",           "#E65100", "#BF360C"),
        ("🛒", "LISTA DE\nSUPERMERCADO",       "lista_supermercado","#6A1B9A", "#4A148C"),
        ("📄", "DIETA\nCOMPLETA",              "dieta_completa",    "#00695C", "#004D40"),
        ("⚠️", "RECOMENDAÇÕES\nIMPORTANTES",  "recomendacoes",     "#B71C1C", "#7F0000"),
    ]

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, corner_radius=0)
        self.state = state
        self.navigate = navigate
        self._build()

    # ── Construção da UI ───────────────────────────────────────────────────────
    def _build(self) -> None:
        self._build_topbar()
        self._build_content()
        self._build_footer()
        # Inicia atualização do contador de hidratação
        self.after(500, self._tick_hydration)

    def _build_topbar(self) -> None:
        bar = ctk.CTkFrame(self, height=64, corner_radius=0, fg_color=("gray88", "gray18"))
        bar.pack(fill="x")
        bar.pack_propagate(False)

        # Botões de acessibilidade (direita → esquerda)
        self.theme_btn = ctk.CTkButton(
            bar, text="🌙 Escuro", width=130, height=42,
            font=self.state.f("small"), fg_color=("gray65", "gray40"),
            command=self._toggle_theme,
        )
        self.theme_btn.pack(side="right", padx=8, pady=11)
        if self.state.dark_mode:
            self.theme_btn.configure(text="☀️ Claro")

        ctk.CTkButton(
            bar, text="A−", width=58, height=42,
            font=self.state.f("body"),
            fg_color=("gray65", "gray40"),
            command=self.state.decrease_font,
        ).pack(side="right", padx=(0, 4), pady=11)

        ctk.CTkButton(
            bar, text="A+", width=58, height=42,
            font=self.state.f("body"),
            fg_color=("gray65", "gray40"),
            command=self.state.increase_font,
        ).pack(side="right", padx=(0, 4), pady=11)

        ctk.CTkLabel(
            bar,
            text="🍽️  Plataforma de Dieta — Vovô Fabio",
            font=self.state.f("heading"),
            anchor="w",
        ).pack(side="left", padx=20, pady=11)

    def _build_content(self) -> None:
        content = ctk.CTkFrame(self, corner_radius=0)
        content.pack(fill="both", expand=True)

        ctk.CTkLabel(
            content,
            text="Bem-vindo! Escolha uma opção abaixo:",
            font=self.state.f("body"),
        ).pack(pady=(20, 6))

        # Grade 2 × 3 de botões
        grid = ctk.CTkFrame(content, corner_radius=0, fg_color="transparent")
        grid.pack(expand=True, pady=10)

        for idx, (icon, label, screen, color, hover) in enumerate(self.BOTOES):
            row, col = divmod(idx, 2)
            txt = f"{icon}\n{label}"
            ctk.CTkButton(
                grid,
                text=txt,
                font=self.state.f("button"),
                width=300,
                height=120,
                corner_radius=14,
                fg_color=color,
                hover_color=hover,
                command=lambda s=screen: self.navigate(s),
            ).grid(row=row, column=col, padx=18, pady=12)

    def _build_footer(self) -> None:
        footer = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color=("gray88", "gray18"))
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)

        self.hydration_label = ctk.CTkLabel(
            footer,
            text="💧  Lembre-se: tome 1 copo de água agora!",
            font=self.state.f("body"),
            text_color="#1565C0",
        )
        self.hydration_label.pack(expand=True)

    # ── Atualização do rodapé ──────────────────────────────────────────────────
    def _tick_hydration(self) -> None:
        timer = self.state.hydration_timer
        cups = self.state.hydration_cups
        countdown = timer.get_countdown_str() if timer else "60:00"
        self.hydration_label.configure(
            text=f"💧  Tome 1 copo de água agora!   •   Copos hoje: {cups}/8   •   Próximo lembrete: {countdown}"
        )
        self.after(1000, self._tick_hydration)

    # ── Tema ───────────────────────────────────────────────────────────────────
    def _toggle_theme(self) -> None:
        self.state.toggle_theme()
        self.theme_btn.configure(text="☀️ Claro" if self.state.dark_mode else "🌙 Escuro")

    def on_show(self) -> None:
        self.theme_btn.configure(text="☀️ Claro" if self.state.dark_mode else "🌙 Escuro")
