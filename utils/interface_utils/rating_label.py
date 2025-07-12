"""Modular label for displaying ratings."""
import customtkinter as ctk


class RatingLabel(ctk.CTkLabel):
    """Label for displaying ratings."""

    font_style = ('Arial', 18, 'bold')

    def __init__(self, parent, rating_to_display):
        """Initialize label."""
        self.background_color = 'white'

        try:
            rating = int(rating_to_display)
            if rating < 40:
                self.background_color = '#f45757'
            elif rating < 60:
                self.background_color = '#f79301'
            elif rating < 70:
                self.background_color = '#e8cd0d'
            elif rating < 85:
                self.background_color = '#65e212'
            elif rating < 100:
                self.background_color = '#05ab8d'
            elif rating < 125:
                self.background_color = '#0091f3'
            elif rating < 150:
                self.background_color = '#9f73ff'
            else:
                self.background_color = '#bf4dff'
        except ValueError:
            pass

        super().__init__(
            parent,
            text=rating_to_display,
            font=self.font_style,
            fg_color=self.background_color
        )
