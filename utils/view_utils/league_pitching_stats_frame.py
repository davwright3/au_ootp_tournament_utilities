"""Frame for displaying league pitching stats from the selected file."""
import customtkinter as ctk
from utils.stats_utils.get_league_pitching_stats import (
    get_league_pitching_stats
)


class LeaguePitchingStatsFrame(ctk.CTkFrame):
    """Custom frame class."""

    def __init__(self, parent):
        """Initialize the frame."""
        super().__init__(parent)

        self.font_style = ('Arial', 18, 'bold')
        league_stats = get_league_pitching_stats()

        self.title_frame = ctk.CTkLabel(
            self,
            text='League Pitching',
            font=self.font_style
        )
        self.title_frame.grid(row=0, column=0, sticky='nsew')

        self.era_label = ctk.CTkLabel(self, text='ERA: ', font=self.font_style)
        self.era_label.grid(row=2, column=0, sticky='nsew')

        self.era_stat_label = ctk.CTkLabel(
            self,
            text=league_stats[0],
            font=self.font_style
        )
        self.era_stat_label.grid(row=2, column=1, sticky='nsew')

        self.krate_label = ctk.CTkLabel(
            self,
            text='K/9: ',
            font=self.font_style
        )
        self.krate_label.grid(row=3, column=0, sticky='nsew')

        self.krate_stat_label = ctk.CTkLabel(
            self,
            text=league_stats[1],
            font=self.font_style
        )
        self.krate_stat_label.grid(row=3, column=1, sticky='nsew')

        self.bbrate_label = ctk.CTkLabel(
            self,
            text='BB/9 ',
            font=self.font_style
        )
        self.bbrate_label.grid(row=4, column=0, sticky='nsew')

        self.bbrate_stat_label = ctk.CTkLabel(
            self,
            text=league_stats[2],
            font=self.font_style
        )
        self.bbrate_stat_label.grid(row=4, column=1, sticky='nsew')

        self.hrrate_label = ctk.CTkLabel(
            self,
            text='HR/9: ',
            font=self.font_style
        )
        self.hrrate_label.grid(row=5, column=0, sticky='nsew')

        self.hrrate_stat_label = ctk.CTkLabel(
            self,
            text=league_stats[3],
            font=self.font_style
        )
        self.hrrate_stat_label.grid(row=5, column=1, sticky='nsew')
