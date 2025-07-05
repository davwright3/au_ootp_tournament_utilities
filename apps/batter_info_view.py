"""App for viewing individual player level data"""
import customtkinter as ctk
from utils.config_utils.settings import settings as settings_module
from utils.view_utils.header_footer_frame import Header, Footer
from utils.view_utils.batter_ratings_frame import BatterRatingsFrame
from utils.view_utils.batter_individual_overall_stats_frame import BatterIndividualStatsFrame
from utils.view_utils.league_batting_stats_frame import LeagueBattingStatsFrame


class BatterInfoView(ctk.CTkToplevel):
    """TopLevel view for BatterInfo.

    Uses CTK TopLevel to create a new window for viewing
    individual player level data.
    """

    def __init__(self, cid, filepath=None, team=None):
        super().__init__()
        print("Team: ", team)
        self.title(f'Details for Batter Card ID: {cid}')
        self.height = settings_module['FileProcessor']['height']
        self.width = settings_module['FileProcessor']['width']
        self.header_footer_height = int(self.height*.1)

        self.geometry(f'{self.width}x{self.height}')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=0)
        self.columnconfigure(5, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        self.filepath = filepath

        self.header_frame = Header(
            self,
            height=self.header_footer_height,
            width=self.width,
            title= f'Details for Card ID: {cid}'
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=5,
            sticky='nsew',
        )

        self.ratings_frame = BatterRatingsFrame(
            self,
            cid_value=cid
        )
        self.ratings_frame.grid(
            row=1,
            column=0,
            columnspan=1,
            sticky='nw',
        )

        self.overall_statistics_frame = BatterIndividualStatsFrame(
            self,
            cid_value=cid,
            df_target=self.filepath
        )
        self.overall_statistics_frame.grid(
            row=1,
            column=2,
            columnspan=1,
            sticky='nsew',
        )

        self.league_stats_frame = LeagueBattingStatsFrame(
            self,
            df_target=self.filepath
        )
        self.league_stats_frame.grid(
            row=1,
            column=3,
            columnspan=1,
            sticky='nsew',
        )

        if team != 'No teams loaded':
            self.player_team_stats_frame = BatterIndividualStatsFrame(
                self,
                cid_value=cid,
                df_target=self.filepath,
                passed_team=team
            )
            self.player_team_stats_frame.grid(
                row=1,
                column=4,
                columnspan=1,
                sticky='nsew',
            )

        self.footer_frame = Footer(
            self,
            height=self.header_footer_height,
            width=self.width,
        )
        self.footer_frame.grid(
            row=3,
            column=0,
            columnspan=5,
            sticky='nsew',
        )


        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)






