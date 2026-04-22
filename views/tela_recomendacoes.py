"""
tela_recomendacoes.py — 5 abas:
  A — Hidratação (timer + contador de copos)
  B — Proteínas  (regras + tracker carne vermelha)
  C — Orientações (lista + alerta crítico)
  D — Suplementação
  E — Sal de Ervas
"""

import tkinter as tk
from datetime import datetime
import customtkinter as ctk
from views import BaseTela
from utils.helpers import load_json, AppState


class TelaRecomendacoes(BaseTela):

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, state, navigate, title="Recomendações Importantes", icon="⚠️")
        self._orientacoes = load_json("orientacoes.json")
        self._supl = load_json("suplementacao.json")
        self._ervas = load_json("tempero_sal_ervas.json")
        self._build_content()

    # ── Abas ───────────────────────────────────────────────────────────────────
    def _build_content(self) -> None:
        tabs = ctk.CTkTabview(self, height=680)
        tabs.pack(fill="both", expand=True, padx=16, pady=(8, 16))

        tabs.add("💧 Hidratação")
        tabs.add("🥩 Proteínas")
        tabs.add("⚠️ Orientações")
        tabs.add("💊 Suplementação")
        tabs.add("🌿 Sal de Ervas")

        self._build_tab_hidratacao(tabs.tab("💧 Hidratação"))
        self._build_tab_proteinas(tabs.tab("🥩 Proteínas"))
        self._build_tab_orientacoes(tabs.tab("⚠️ Orientações"))
        self._build_tab_suplementacao(tabs.tab("💊 Suplementação"))
        self._build_tab_ervas(tabs.tab("🌿 Sal de Ervas"))

    # ══════════════════════════════════════════════════════════════════════════
    # ABA A — Hidratação
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_hidratacao(self, tab) -> None:
        scroll = ctk.CTkScrollableFrame(tab)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll,
            text="💧  Meta de Hidratação",
            font=self.state.f("heading"),
            anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 4))

        ctk.CTkLabel(
            scroll,
            text="Beba pelo menos 1 copo de água a cada hora.\nMeta diária: 8 copos (2 litros de água).",
            font=self.state.f("body"),
            anchor="w",
            justify="left",
            wraplength=900,
        ).pack(fill="x", padx=18, pady=6)

        # ── Timer countdown ────────────────────────────────────────────────────
        timer_frame = ctk.CTkFrame(scroll, corner_radius=12, fg_color=("gray92", "gray22"))
        timer_frame.pack(fill="x", padx=12, pady=(12, 4))

        ctk.CTkLabel(
            timer_frame,
            text="Próximo lembrete em:",
            font=self.state.f("body"),
            text_color=("gray40", "gray70"),
        ).pack(pady=(12, 2))

        self._countdown_lbl = ctk.CTkLabel(
            timer_frame,
            text="60:00",
            font=ctk.CTkFont(size=52, weight="bold"),
            text_color="#1565C0",
        )
        self._countdown_lbl.pack(pady=4)

        ctk.CTkButton(
            timer_frame,
            text="🔄  Reiniciar Timer",
            font=self.state.f("body"),
            height=46,
            width=220,
            fg_color=("gray65", "gray40"),
            command=self._reset_timer,
        ).pack(pady=(4, 14))

        # ── Contador de copos ─────────────────────────────────────────────────
        cup_frame = ctk.CTkFrame(scroll, corner_radius=12, fg_color=("gray92", "gray22"))
        cup_frame.pack(fill="x", padx=12, pady=8)

        ctk.CTkLabel(
            cup_frame,
            text="Copos de água hoje:",
            font=self.state.f("body"),
            text_color=("gray40", "gray70"),
        ).pack(pady=(12, 2))

        self._cups_lbl = ctk.CTkLabel(
            cup_frame,
            text=f"{self.state.hydration_cups} / 8",
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color="#2E7D32",
        )
        self._cups_lbl.pack(pady=4)

        self._cups_bar = ctk.CTkProgressBar(cup_frame, width=400, height=24)
        self._cups_bar.set(self.state.hydration_cups / 8)
        self._cups_bar.pack(pady=4)

        ctk.CTkButton(
            cup_frame,
            text="✅  Bebi meu copo!",
            font=self.state.f("button"),
            height=56,
            width=260,
            fg_color="#1565C0",
            hover_color="#0D47A1",
            command=self._add_cup,
        ).pack(pady=(8, 14))

        # Registrar callback para atualizar display quando timer disparar
        self.state.register_cup_callback(self._refresh_cups)
        self.after(500, self._tick_display)

    def _tick_display(self) -> None:
        timer = self.state.hydration_timer
        if timer and hasattr(self, "_countdown_lbl"):
            self._countdown_lbl.configure(text=timer.get_countdown_str())
        self.after(1000, self._tick_display)

    def _add_cup(self) -> None:
        self.state.add_cup()
        self._refresh_cups(self.state.hydration_cups)
        if self.state.hydration_timer:
            self.state.hydration_timer.reset()

    def _reset_timer(self) -> None:
        if self.state.hydration_timer:
            self.state.hydration_timer.reset()

    def _refresh_cups(self, cups: int) -> None:
        if hasattr(self, "_cups_lbl"):
            self._cups_lbl.configure(text=f"{cups} / 8")
            self._cups_bar.set(min(cups / 8, 1.0))

    # ══════════════════════════════════════════════════════════════════════════
    # ABA B — Proteínas
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_proteinas(self, tab) -> None:
        scroll = ctk.CTkScrollableFrame(tab)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll, text="🥩  Regras de Proteína",
            font=self.state.f("heading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 4))

        regras = [
            self._orientacoes.get("regra_proteina", ""),
            self._orientacoes.get("regra_carne_vermelha", ""),
        ]
        for r in regras:
            if r:
                row = ctk.CTkFrame(scroll, corner_radius=10, fg_color=("gray92", "gray22"))
                row.pack(fill="x", padx=10, pady=6)
                ctk.CTkLabel(
                    row, text=f"  ✅  {r}",
                    font=self.state.f("body"), anchor="w",
                    wraplength=900, justify="left",
                ).pack(fill="x", padx=12, pady=12)

        # Tracker carne vermelha
        ctk.CTkLabel(
            scroll, text="📅  Controle de Carne Vermelha na Semana:",
            font=self.state.f("subheading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(18, 4))

        dias_pt = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        tracker_frame = ctk.CTkFrame(scroll, corner_radius=10, fg_color=("gray92", "gray22"))
        tracker_frame.pack(fill="x", padx=10, pady=6)

        self._meat_vars: list[tk.BooleanVar] = []
        self._meat_count_lbl: ctk.CTkLabel | None = None

        days_row = ctk.CTkFrame(tracker_frame, fg_color="transparent")
        days_row.pack(fill="x", padx=12, pady=12)

        for dia in dias_pt:
            var = tk.BooleanVar(value=dia in self.state.red_meat_days)
            self._meat_vars.append(var)
            cb = ctk.CTkCheckBox(
                days_row,
                text=dia,
                variable=var,
                font=self.state.f("body"),
                checkbox_width=28,
                checkbox_height=28,
                command=self._update_meat_tracker,
            )
            cb.pack(side="left", padx=8, pady=4)

        self._meat_count_lbl = ctk.CTkLabel(
            tracker_frame,
            text=self._meat_tracker_text(),
            font=self.state.f("subheading"),
            anchor="center",
        )
        self._meat_count_lbl.pack(pady=(4, 14))

    def _update_meat_tracker(self) -> None:
        dias_pt = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        self.state.red_meat_days = {
            dias_pt[i] for i, v in enumerate(self._meat_vars) if v.get()
        }
        if self._meat_count_lbl:
            self._meat_count_lbl.configure(text=self._meat_tracker_text())

    def _meat_tracker_text(self) -> str:
        count = len(self.state.red_meat_days)
        color_hint = "⚠️ " if count >= 3 else ""
        return f"{color_hint}Carne vermelha esta semana: {count}/3 dias"

    # ══════════════════════════════════════════════════════════════════════════
    # ABA C — Orientações
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_orientacoes(self, tab) -> None:
        scroll = ctk.CTkScrollableFrame(tab)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # !! ALERTA CRÍTICO !!
        alerta_frame = ctk.CTkFrame(scroll, corner_radius=12, fg_color="#B71C1C")
        alerta_frame.pack(fill="x", padx=10, pady=(10, 12))
        ctk.CTkLabel(
            alerta_frame,
            text="⚠️  ATENÇÃO — FRUTAS TÓXICAS PARA PACIENTES RENAIS",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="white",
        ).pack(pady=(14, 4))
        ctk.CTkLabel(
            alerta_frame,
            text="NUNCA CONSUMA  CARAMBOLA  e  BIRIRI\nEstas frutas são tóxicas para pacientes com doença renal crônica.",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#FFCDD2",
            justify="center",
        ).pack(pady=(2, 14))

        ctk.CTkLabel(
            scroll, text="📋  Orientações Gerais:",
            font=self.state.f("heading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 4))

        for i, o in enumerate(self._orientacoes.get("orientacoes_gerais", []), 1):
            row = ctk.CTkFrame(scroll, corner_radius=10, fg_color=("gray92", "gray22"))
            row.pack(fill="x", padx=10, pady=5)
            ctk.CTkLabel(
                row,
                text=f"  {i}.  {o}",
                font=self.state.f("body"),
                anchor="nw",
                justify="left",
                wraplength=900,
            ).pack(fill="x", padx=14, pady=12)

        # Alimentos proibidos
        proib = self._orientacoes.get("alimentos_proibidos_sodio", {})
        if proib:
            ctk.CTkLabel(
                scroll,
                text=f"🚫  {proib.get('titulo', 'Alimentos NÃO recomendados')}:",
                font=self.state.f("subheading"),
                anchor="w",
                text_color=("#B71C1C", "#EF9A9A"),
            ).pack(fill="x", padx=12, pady=(16, 4))

            for item in proib.get("itens", []):
                ctk.CTkLabel(
                    scroll,
                    text=f"  ❌  {item}",
                    font=self.state.f("body"),
                    anchor="nw",
                    justify="left",
                    wraplength=950,
                ).pack(fill="x", padx=20, pady=3)

    # ══════════════════════════════════════════════════════════════════════════
    # ABA D — Suplementação
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_suplementacao(self, tab) -> None:
        scroll = ctk.CTkScrollableFrame(tab)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll, text="💊  Suplementação Prescrita",
            font=self.state.f("heading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 6))

        colors = ["#1565C0", "#2E7D32"]
        for idx, s in enumerate(self._supl.get("suplementos", [])):
            card = ctk.CTkFrame(scroll, corner_radius=14, fg_color=colors[idx % len(colors)])
            card.pack(fill="x", padx=10, pady=8)

            ctk.CTkLabel(
                card,
                text=f"{s.get('icone', '💊')}  {s.get('nome', '')}",
                font=self.state.f("subheading"),
                text_color="white",
                anchor="w",
            ).pack(fill="x", padx=18, pady=(14, 4))

            ctk.CTkLabel(
                card,
                text=f"🕐  Horário: {s.get('horario', '')}",
                font=self.state.f("body"),
                text_color="#BBDEFB",
                anchor="w",
            ).pack(fill="x", padx=22, pady=2)

            ctk.CTkLabel(
                card,
                text=f"📋  {s.get('modo_uso', '')}",
                font=self.state.f("body"),
                text_color="white",
                anchor="nw",
                justify="left",
                wraplength=900,
            ).pack(fill="x", padx=22, pady=(2, 14))

        # Onde comprar
        ctk.CTkLabel(
            scroll, text="🛒  Onde Comprar:",
            font=self.state.f("subheading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(16, 4))

        for contato in self._supl.get("onde_comprar", []):
            ctk.CTkLabel(
                scroll,
                text=f"  📞  {contato}",
                font=self.state.f("body"),
                anchor="w",
            ).pack(fill="x", padx=18, pady=3)

        ctk.CTkLabel(
            scroll,
            text=f"\n📅 Prescrito em: {self._supl.get('data_prescricao', '')} — {self._supl.get('nutricionista', '')}",
            font=self.state.f("small"),
            text_color=("gray40", "gray65"),
            anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 16))

    # ══════════════════════════════════════════════════════════════════════════
    # ABA E — Sal de Ervas
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_ervas(self, tab) -> None:
        scroll = ctk.CTkScrollableFrame(tab)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll, text=f"🌿  {self._ervas.get('nome', 'Sal de Ervas')}",
            font=self.state.f("heading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 4))

        # Destaque
        dest_frame = ctk.CTkFrame(scroll, corner_radius=12, fg_color="#004D40")
        dest_frame.pack(fill="x", padx=10, pady=6)
        ctk.CTkLabel(
            dest_frame,
            text="✅  Substitui o sal comum e é saudável para os rins!",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#A5D6A7",
        ).pack(pady=14)

        # Descrição
        ctk.CTkLabel(
            scroll,
            text=self._ervas.get("descricao", ""),
            font=self.state.f("body"),
            anchor="nw",
            justify="left",
            wraplength=950,
        ).pack(fill="x", padx=16, pady=8)

        # Ingredientes
        ctk.CTkLabel(
            scroll, text="Ingredientes:",
            font=self.state.f("subheading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(10, 4))

        for ing in self._ervas.get("ingredientes", []):
            ctk.CTkLabel(
                scroll, text=f"  •  {ing}",
                font=self.state.f("body"), anchor="w",
            ).pack(fill="x", padx=20, pady=3)

        # Modo de preparo
        ctk.CTkLabel(
            scroll, text="Modo de Preparo:",
            font=self.state.f("subheading"), anchor="w",
        ).pack(fill="x", padx=12, pady=(14, 4))

        for i, passo in enumerate(self._ervas.get("modo_preparo", []), 1):
            row = ctk.CTkFrame(scroll, corner_radius=8, fg_color=("gray92", "gray22"))
            row.pack(fill="x", padx=10, pady=4)
            ctk.CTkLabel(
                row, text=f"  {i}.  {passo}",
                font=self.state.f("body"), anchor="w",
                wraplength=920, justify="left",
            ).pack(fill="x", padx=12, pady=10)

        # Informação nutricional
        nut = self._ervas.get("informacao_nutricional_por_porcao_1g", {})
        if nut:
            ctk.CTkLabel(
                scroll, text="Informação Nutricional (por porção de 1g):",
                font=self.state.f("subheading"), anchor="w",
            ).pack(fill="x", padx=12, pady=(14, 4))

            nutri_data = [
                ("Energia", f"{nut.get('energia_kcal', 0)} kcal"),
                ("Carboidratos", f"{nut.get('carboidratos_g', 0)} g"),
                ("Proteínas", f"{nut.get('proteina_g', 0)} g"),
                ("Gorduras totais", f"{nut.get('gordura_g', 0)} g"),
                ("Fibra alimentar", f"{nut.get('fibra_alimentar_g', 0)} g"),
                ("Sódio", f"{nut.get('sodio_mg', 0)} mg"),
            ]
            nutri_frame = ctk.CTkFrame(scroll, corner_radius=10, fg_color=("gray92", "gray22"))
            nutri_frame.pack(fill="x", padx=10, pady=6)
            for lbl, val in nutri_data:
                row = ctk.CTkFrame(nutri_frame, fg_color="transparent")
                row.pack(fill="x", padx=14, pady=4)
                ctk.CTkLabel(row, text=lbl, font=self.state.f("body"), anchor="w", width=200).pack(side="left")
                ctk.CTkLabel(row, text=val, font=ctk.CTkFont(size=18, weight="bold"), anchor="w").pack(side="left")

        # Benefícios
        beneficios = self._ervas.get("beneficios", [])
        if beneficios:
            ctk.CTkLabel(
                scroll, text="Benefícios:",
                font=self.state.f("subheading"), anchor="w",
            ).pack(fill="x", padx=12, pady=(14, 4))
            for b in beneficios:
                ctk.CTkLabel(
                    scroll, text=f"  ✅  {b}",
                    font=self.state.f("body"), anchor="w",
                    wraplength=950,
                ).pack(fill="x", padx=20, pady=3)

        ctk.CTkLabel(scroll, text="").pack(pady=10)  # spacer
