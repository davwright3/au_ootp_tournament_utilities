"""Custom button for selecting positions to view."""
import customtkinter as ctk


class CustomPositionButton(ctk.CTkButton):
    """Create a button to choose the position."""

    def __init__(self, parent, text="Position", command=None, **kwargs):
        """Initialize button."""
        super().__init__(parent, text=text, command=command, **kwargs)
        self.configure(
            fg_color='blue',
            hover_color='red',
            text_color='white',
            corner_radius=10,
            font=("Arial", 12)
        )
