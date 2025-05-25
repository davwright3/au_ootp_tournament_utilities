"""Create button to open app module."""
import customtkinter as ctk


class AppSelectButton(ctk.CTkButton):
    """Create button to open app module."""

    def __init__(self, parent, text="Button", command=None, **kwargs):
        """Initialize button."""
        super().__init__(parent, text=text, command=command, **kwargs)
        self.configure(
            fg_color="blue",
            hover_color="red",
            text_color="white",
            corner_radius=10,
            font=("Arial", 14, "bold")
        )
