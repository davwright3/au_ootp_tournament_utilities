"""App for viewing individual player level data"""
import customtkinter as ctk
from pygments.lexers import q

from utils.config_utils.settings import settings as settings_module
from utils.view_utils.header_footer_frame import Header, Footer
from utils.view_utils.batter_ratings_frame import BatterRatingsFrame
from utils.view_utils.batter_individual_overall_stats_frame import BatterIndividualStatsFrame
from utils.view_utils.league_batting_stats_frame import LeagueBattingStatsFrame
from utils.view_utils.batter_stat_plot_frame import BatterStatPlotFrame
from utils.stats_utils.get_player_df import get_player_df
from utils.data_utils.data_store import data_store

class BatterInfoView(ctk.CTkToplevel):
    """TopLevel view for BatterInfo.

    Uses CTK TopLevel to create a new window for viewing
    individual player level data.
    """

    def __init__(self, cid, filepath=None, team=None):
        super().__init__()
        self.title(f'Details for Batter Card ID: {cid}')
        self.height = settings_module['FileProcessor']['height']
        self.width = settings_module['FileProcessor']['width']
        self.header_footer_height = int(self.height*.1)

        self.geometry(f'{self.width}x{self.height}')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        # self.columnconfigure(4, weight=0)

        self.rowconfigure(0, minsize=self.header_footer_height)
        self.rowconfigure(1, weight=0, minsize=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, minsize=self.header_footer_height)

        self.filepath = filepath
        self.player_df = get_player_df(self.filepath, cid)

        self.header_frame = Header(
            self,
            height=self.header_footer_height,
            width=self.width,
            title= f'Details for Card ID: {cid}'
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky='nsew',
        )

        self.top_stats_frame = ctk.CTkFrame(self)
        self.top_stats_frame.grid(row=1, column=0, columnspan=4, sticky='nsew')
        for col in range(4):
            self.top_stats_frame.columnconfigure(col, weight=1)

        self.ratings_frame = BatterRatingsFrame(
            self.top_stats_frame,
            cid_value=cid
        )
        self.ratings_frame.grid(
            row=0,
            column=0,
            columnspan=1,
            sticky='n',
        )

        self.overall_statistics_frame = BatterIndividualStatsFrame(
            self.top_stats_frame,
            cid_value=cid,
            player_df=self.player_df,
        )
        self.overall_statistics_frame.grid(
            row=0,
            column=1,
            columnspan=1,
            sticky='nsew',
        )

        # if team != 'No teams loaded':
        self.player_team_stats_frame = BatterIndividualStatsFrame(
            self.top_stats_frame,
            cid_value=cid,
            player_df=self.player_df,
            passed_team=team
        )
        self.player_team_stats_frame.grid(
            row=0,
            column=2,
            columnspan=1,
            sticky='nsew',
        )


        self.league_stats_frame = LeagueBattingStatsFrame(
            self.top_stats_frame,
        )
        self.league_stats_frame.grid(
            row=0,
            column=3,
            columnspan=1,
            sticky='nsew',
        )


        self.batter_plot_frame = BatterStatPlotFrame(
            self,
            card_id=cid,
        )
        self.batter_plot_frame.grid(
            row=2,
            column=0,
            columnspan=4,
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
            columnspan=4,
            sticky='nsew',
        )


        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def show_and_release_topmost():
            """Lift window, set topmost and then release safely."""
            if not self.winfo_exists():
                return

            try:
                self.lift()
                self.attributes("-topmost", True)
            except Exception():
                return

            def release():
                if self.winfo_exists():
                    try:
                        self.attributes("-topmost", False)
                    except Exception:
                        pass

            self.after(100, release)

        def on_app_close():
            print("Running on app close")
            try:
                if hasattr(self, 'batter_plot_frame'):
                    self.batter_plot_frame.destroy()
            except Exception:
                print("Error destroying batter_plot_frame")

            self.destroy()

        show_and_release_topmost()
        self.protocol('WM_DELETE_WINDOW', on_app_close)






