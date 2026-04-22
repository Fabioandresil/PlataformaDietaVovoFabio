"""Views da Plataforma de Dieta — Vovô Fabio."""

import customtkinter as ctk


class BaseTela(ctk.CTkFrame):
    """Frame base com cabeçalho padrão (botão Voltar + título) para todas as telas."""

    def __init__(self, parent, state, navigate, title: str, icon: str = ""):
        super().__init__(parent, corner_radius=0)
        self.state = state
        self.navigate = navigate
        self._build_header(title, icon)

    def _build_header(self, title: str, icon: str) -> ctk.CTkFrame:
        header = ctk.CTkFrame(self, height=72, corner_radius=0, fg_color=("gray88", "gray18"))
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        ctk.CTkButton(
            header,
            text="← Voltar",
            width=130,
            height=46,
            font=self.state.f("body"),
            fg_color=("gray70", "gray35"),
            hover_color=("gray60", "gray45"),
            command=lambda: self.navigate("principal"),
        ).pack(side="left", padx=16, pady=13)

        ctk.CTkLabel(
            header,
            text=f"{icon}  {title}",
            font=self.state.f("heading"),
            anchor="w",
        ).pack(side="left", padx=10, pady=13)

        return header

    def on_show(self) -> None:
        """Chamado ao exibir a tela. Sobrescrever se necessário."""
        pass
