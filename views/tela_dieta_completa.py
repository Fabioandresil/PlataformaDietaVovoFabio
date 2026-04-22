"""
tela_dieta_completa.py — Exibe o plano alimentar completo prescrito pela
nutricionista, com informações do paciente no topo.
"""

import customtkinter as ctk
from views import BaseTela
from utils.helpers import load_json, AppState


class TelaDietaCompleta(BaseTela):

    def __init__(self, parent, state: AppState, navigate):
        super().__init__(parent, state, navigate, title="Dieta Completa", icon="📄")
        self._plano = load_json("plano_alimentar.json")
        self._supl = load_json("suplementacao.json")
        self._build_content()

    # ── Conteúdo ───────────────────────────────────────────────────────────────
    def _build_content(self) -> None:
        scroll = ctk.CTkScrollableFrame(self)
        scroll.pack(fill="both", expand=True, padx=16, pady=(8, 4))

        self._patient_header(scroll)
        self._divider(scroll)

        for ref in self._plano.get("refeicoes", []):
            self._refeicao_block(scroll, ref)
            self._divider(scroll)

        self._suplementacao_block(scroll)

        # Rodapé
        ctk.CTkLabel(
            scroll,
            text="Nutricionista: Verônica Alves — CRN/1 20331 — NefroClínicas Brasília-DF",
            font=self.state.f("small"),
            text_color=("gray40", "gray65"),
        ).pack(pady=(8, 20))

    # ── Cabeçalho do paciente ──────────────────────────────────────────────────
    def _patient_header(self, parent) -> None:
        frame = ctk.CTkFrame(parent, corner_radius=12, fg_color=("gray93", "gray22"))
        frame.pack(fill="x", padx=6, pady=(6, 2))

        ctk.CTkLabel(
            frame,
            text=f"👤 {self._plano.get('paciente', '')}",
            font=self.state.f("heading"),
            anchor="w",
        ).pack(fill="x", padx=18, pady=(14, 4))

        info = [
            f"Idade: {self._plano.get('idade', '')} anos  •  Nascimento: {self._plano.get('data_nascimento', '')}",
            f"Altura: {self._plano.get('altura_cm', '')} cm  •  Peso: {self._plano.get('peso_kg', '')} kg  •  IMC: {self._plano.get('imc', '')}",
            f"Atividade física: {self._plano.get('atividade_fisica', '')}",
        ]
        conds = "  |  ".join(self._plano.get("condicoes_saude", []))
        info.append(f"Condições de saúde: {conds}")

        for line in info:
            ctk.CTkLabel(
                frame,
                text=line,
                font=self.state.f("body"),
                anchor="w",
                wraplength=1100,
                justify="left",
            ).pack(fill="x", padx=18, pady=2)

        ctk.CTkLabel(frame, text="", height=8).pack()  # spacer

    # ── Bloco de refeição ──────────────────────────────────────────────────────
    def _refeicao_block(self, parent, ref: dict) -> None:
        # Título
        ctk.CTkLabel(
            parent,
            text=f"🕐 {ref.get('horario', '')}  —  {ref.get('nome', '')}",
            font=self.state.f("subheading"),
            anchor="w",
        ).pack(fill="x", padx=14, pady=(10, 4))

        # Entrada (almoço)
        for ent in ref.get("entrada", []):
            ctk.CTkLabel(
                parent,
                text=f"  🥗  {ent}",
                font=self.state.f("body"),
                anchor="w",
                wraplength=1100,
            ).pack(fill="x", padx=24, pady=2)

        # Itens
        for item in ref.get("itens", []):
            opcoes = "  /  ".join(item.get("opcoes", []))
            ctk.CTkLabel(
                parent,
                text=f"  • {item.get('descricao', '')}: {opcoes}",
                font=self.state.f("body"),
                anchor="w",
                wraplength=1100,
                justify="left",
            ).pack(fill="x", padx=24, pady=2)

        # Notas
        for nota in ref.get("notas", []):
            ctk.CTkLabel(
                parent,
                text=f"  📌 {nota}",
                font=self.state.f("small"),
                anchor="w",
                text_color=("gray40", "gray65"),
                wraplength=1100,
                justify="left",
            ).pack(fill="x", padx=30, pady=2)

    # ── Suplementação ──────────────────────────────────────────────────────────
    def _suplementacao_block(self, parent) -> None:
        ctk.CTkLabel(
            parent,
            text="💊  Suplementação",
            font=self.state.f("subheading"),
            anchor="w",
        ).pack(fill="x", padx=14, pady=(10, 4))

        for s in self._supl.get("suplementos", []):
            ctk.CTkLabel(
                parent,
                text=f"  • {s.get('nome', '')}: {s.get('modo_uso', '')}",
                font=self.state.f("body"),
                anchor="w",
                wraplength=1100,
                justify="left",
            ).pack(fill="x", padx=24, pady=2)

    # ── Utilitário ─────────────────────────────────────────────────────────────
    def _divider(self, parent) -> None:
        ctk.CTkFrame(parent, height=2, fg_color=("gray75", "gray35")).pack(
            fill="x", padx=14, pady=4
        )
