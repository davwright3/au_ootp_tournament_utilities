"""Modular label for displaying ratings."""
import customtkinter as ctk


class RatingLabel(ctk.CTkLabel):
    """Label for displaying ratings."""

    font_style = ('Arial', 18, 'bold')

    def __init__(self, parent, rating_to_display):
        """Initialize label."""
        super().__init__(
            parent,
            text = rating_to_display,
            font = self.font_style
        )