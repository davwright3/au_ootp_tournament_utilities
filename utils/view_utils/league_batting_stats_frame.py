"""Custom frame for displaying league batting stats."""
import customtkinter as ctk
from utils.data_utils.league_batting_stats import league_stats


class LeagueBattingStatsFrame(ctk.CTkFrame):
    """Frame for displaying league batting stats."""

    def __init__(self, parent):
        """Initialize the frame."""
        super().__init__(parent)

        league_stats_display = league_stats.get_league_pitching_stats()
        self.font_style = ("Arial", 18, 'bold')

        row = 0
        league_stats_label = ctk.CTkLabel(
            self,
            text="League Batting Stats",
            font=self.font_style
        )
        league_stats_label.grid(
            row=row,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )
        row += 1

        league_avg_label = ctk.CTkLabel(
            self,
            text="Avg:",
            font=self.font_style,
            justify="right"
        )
        league_avg_label.grid(row=row, column=0, padx=2, pady=2, sticky="nsew")

        league_avg_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[0],
            font=self.font_style,
            justify="left"
        )
        league_avg_stat.grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
        row += 1

        league_obp_label = ctk.CTkLabel(
            self,
            text="OBP:",
            font=self.font_style,
            justify="right"
        )
        league_obp_label.grid(row=row, column=0, padx=2, pady=2, sticky="nsew")

        league_obp_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[1],
            font=self.font_style,
            justify="left"
        )
        league_obp_stat.grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
        row += 1

        league_slg_label = ctk.CTkLabel(
            self,
            text="SLG:",
            font=self.font_style,
            justify="right"
        )
        league_slg_label.grid(row=row, column=0, padx=2, pady=2, sticky="nsew")

        league_slg_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[2],
            font=self.font_style,
            justify="left"
        )
        league_slg_stat.grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
        row += 1

        league_ops_label = ctk.CTkLabel(
            self,
            text="OPS:",
            font=self.font_style,
            justify="right"
        )
        league_ops_label.grid(row=row, column=0, padx=2, pady=2, sticky="nsew")

        league_ops_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[3],
            font=self.font_style,
            justify="left"
        )
        league_ops_stat.grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
        row += 1

        league_woba_label = ctk.CTkLabel(
            self,
            text="WOBA:",
            font=self.font_style,
            justify="right"
        )
        league_woba_label.grid(
            row=row,
            column=0,
            padx=2,
            pady=2,
            sticky="nsew")

        league_woba_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[4],
            font=self.font_style,
            justify="left"
        )
        league_woba_stat.grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
        row += 1

        league_hr_label = ctk.CTkLabel(
            self,
            text="HR/600:",
            font=self.font_style,
            justify="right"
        )
        league_hr_label.grid(row=row, column=0, padx=2, pady=2, sticky="nsew")

        league_hr_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[5],
            font=self.font_style,
            justify="left"
        )
        league_hr_stat.grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
        row += 1

        league_strikeout_label = ctk.CTkLabel(
            self,
            text="K/600:",
            font=self.font_style,
            justify="right"
        )
        league_strikeout_label.grid(
            row=row,
            column=0,
            padx=2,
            pady=2,
            sticky="nsew"
        )

        league_strikeout_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[6],
            font=self.font_style,
            justify="left"
        )
        league_strikeout_stat.grid(
            row=row,
            column=1,
            padx=2,
            pady=2,
            sticky="nsew"
        )
        row += 1

        league_walk_label = ctk.CTkLabel(
            self,
            text="BB/600:",
            font=self.font_style,
            justify="right"
        )
        league_walk_label.grid(
            row=row,
            column=0,
            padx=2,
            pady=2,
            sticky="nsew"
        )

        league_walk_stat = ctk.CTkLabel(
            self,
            text=league_stats_display[7],
            font=self.font_style,
            justify="left"
        )
        league_walk_stat.grid(
            row=row,
            column=1,
            padx=2,
            pady=2,
            sticky="nsew"
        )
