"""Frame for displaying individual batter stats."""
import customtkinter as ctk
from utils.stats_utils.get_individual_batter_stats import get_individual_batter_stats
import time


class BatterIndividualStatsFrame(ctk.CTkFrame):
    """Frame for displaying individual batter stats."""
    def __init__(self, parent, cid_value=None, df_target=None, player_df=None, passed_team=None):
        super().__init__(parent, border_width=2, border_color='black')

        self.batter_stats = get_individual_batter_stats(cid_value, player_df)

        if passed_team != 'No teams loaded':
            returned_stats = get_individual_batter_stats(cid_value, player_df, team=passed_team)
            if returned_stats is None:
                self.batter_stats = [.000, .000, .000, .000, .000, 0.0, 0.0, 0.0, 0]
            else:
                self.batter_stats = returned_stats

        self.font_style = ("Arial", 18, 'bold')


        average_display = f"{self.batter_stats[0]:.3f}"[1:]
        obp_display = f"{self.batter_stats[1]:.3f}"[1:]
        slg_display = f"{self.batter_stats[2]:.3f}"[1:]
        ops_display = f"{self.batter_stats[3]:.3f}"[1:]
        woba_display = f"{self.batter_stats[4]:.3f}"[1:]
        hr_display = f"{self.batter_stats[5]:.2f}"
        k_display = f"{self.batter_stats[6]:.2f}"
        bb_display = f"{self.batter_stats[7]:.2f}"
        plate_app_display = f"{self.batter_stats[8]}"

        row=0
        if passed_team is None:
            self.batter_label = ctk.CTkLabel(
                self,
                text="Overall Stats",
                font=self.font_style,
            )
            self.batter_label.grid(row=row, column=0, columnspan=2, padx=10, pady=10)
            row+=1
        else:
            self.batter_label = ctk.CTkLabel(
                self,
                text="Team Stats",
                font=self.font_style,
            )
            self.batter_label.grid(row=row, column=0, columnspan=2, padx=10, pady=10)
            row += 1

        self.average_label = ctk.CTkLabel(
            self,
            text="AVG:",
            font=self.font_style,
            justify="right",
        )
        self.average_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.avg_stat = ctk.CTkLabel(
            self,
            text=average_display,
            font=self.font_style,
            justify="left",
        )
        self.avg_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.obp_label = ctk.CTkLabel(
            self,
            text="OBP:",
            font=self.font_style,
            justify="right",
        )
        self.obp_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.obp_stat = ctk.CTkLabel(
            self,
            text=obp_display,
            font=self.font_style,
            justify="left",
        )
        self.obp_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.slg_label = ctk.CTkLabel(
            self,
            text="SLG:",
            font=self.font_style,
            justify="right",
        )
        self.slg_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.slg_stat = ctk.CTkLabel(
            self,
            text=slg_display,
            font=self.font_style,
            justify="left",
        )
        self.slg_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.ops_label = ctk.CTkLabel(
            self,
            text="OPS:",
            font=self.font_style,
            justify="right",
        )
        self.ops_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.ops_stat = ctk.CTkLabel(
            self,
            text=ops_display,
            font=self.font_style,
            justify="left",
        )
        self.ops_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.woba_label = ctk.CTkLabel(
            self,
            text="wOBA:",
            font=self.font_style,
            justify="right",
        )
        self.woba_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.woba_stat = ctk.CTkLabel(
            self,
            text=woba_display,
            font=self.font_style,
            justify="left",
        )
        self.woba_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.hr_label = ctk.CTkLabel(
            self,
            text="HR/600:",
            font=self.font_style,
            justify="right",
        )
        self.hr_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.hr_stat = ctk.CTkLabel(
            self,
            text=hr_display,
            font=self.font_style,
            justify="left",
        )
        self.hr_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.strikeout_label = ctk.CTkLabel(
            self,
            text="K/600:",
            font=self.font_style,
            justify="right",
        )
        self.strikeout_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.strikeout_stat = ctk.CTkLabel(
            self,
            text=k_display,
            font=self.font_style,
            justify="left",
        )
        self.strikeout_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.walks_label = ctk.CTkLabel(
            self,
            text="BB/600:",
            font=self.font_style,
            justify="right",
        )
        self.walks_label.grid(
            row=row, column=0, padx=2, pady=2, sticky='nsew'
        )

        self.walks_stat = ctk.CTkLabel(
            self,
            text=bb_display,
            font=self.font_style,
            justify="left",
        )
        self.walks_stat.grid(
            row=row, column=1, padx=2, pady=2, sticky='nsew'
        )
        row += 1

        self.plate_appearances_label = ctk.CTkLabel(self, text="PA", font=self.font_style, justify="right")
        self.plate_appearances_label.grid(row=row, column=0, padx=2, pady=2, sticky='nsew')

        self.plate_appearances_stat = ctk.CTkLabel(self, text=plate_app_display, font=self.font_style, justify="left")
        self.plate_appearances_stat.grid(row=row, column=1, padx=2, pady=2, sticky='nsew')
        row += 1

