"""Frame for displaying individual pitcher stats."""
import customtkinter as ctk
from utils.stats_utils.get_individual_pitcher_stats import get_individual_pitcher_stats


class PitcherIndividualStatsFrame(ctk.CTkFrame):
    """Frame for displaying individual pitcher stats."""
    def __init__(self, parent, cid_value, team=None):
        """Initialize the frame"""
        super().__init__(parent)

        self.pitcher_stats = []

        self.font_style = ("Arial", 18, 'bold')
        if team is not None:
            self.main_label = ctk.CTkLabel(self, text=team, font=self.font_style)
            self.main_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
            self.pitcher_stats = get_individual_pitcher_stats(cid_value, team=team)
        else:
            self.main_label = ctk.CTkLabel(self, text="Overall", font=self.font_style)
            self.main_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
            self.pitcher_stats = get_individual_pitcher_stats(cid_value)

        self.innings_label = ctk.CTkLabel(self, text='IP: ', font=self.font_style)
        self.innings_label.grid(row=1, column=0, sticky='e')

        self.inning_stat_label = ctk.CTkLabel(
            self,
            text=self.pitcher_stats[0],
            font=self.font_style
        )
        self.inning_stat_label.grid(
            row=1,
            column=1,
            sticky='w'
        )

        self.era_label = ctk.CTkLabel(
            self,
            text='ERA: ',
            font=self.font_style
        )
        self.era_label.grid(
            row=2,
            column=0,
            sticky='e'
        )

        self.era_stat_label = ctk.CTkLabel(
            self,
            text=self.pitcher_stats[1],
            font=self.font_style
        )
        self.era_stat_label.grid(
            row=2,
            column=1,
            sticky='w'
        )

        self.strikeout_label = ctk.CTkLabel(
            self,
            text='K/9: ',
            font=self.font_style
        )
        self.strikeout_label.grid(
            row=3,
            column=0,
            sticky='e'
        )

        self.strikeout_stat_label = ctk.CTkLabel(
            self,
            text=self.pitcher_stats[2],
            font=self.font_style
        )
        self.strikeout_stat_label.grid(
            row=3,
            column=1,
            sticky='w'
        )


        self.walk_label = ctk.CTkLabel(
            self,
            text="BB/9: ",
            font=self.font_style
        )
        self.walk_label.grid(row=4, column=0, sticky='e')

        self.walk_stat_label = ctk.CTkLabel(self, text=self.pitcher_stats[3], font=self.font_style)
        self.walk_stat_label.grid(row=4, column=1, sticky='w')

        self.hr_label = ctk.CTkLabel(self, text='HR/9: ', font=self.font_style)
        self.hr_label.grid(row=5, column=0, sticky='e')

        self.hr_stat_label = ctk.CTkLabel(self, text=self.pitcher_stats[4], font=self.font_style)
        self.hr_stat_label.grid(row=5, column=1, sticky='w')



