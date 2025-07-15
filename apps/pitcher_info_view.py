"""View for individual pitcher data."""
import customtkinter as ctk
from utils.config_utils.settings import settings as settings_module
from utils.view_utils.header_footer_frame import Header, Footer
from utils.data_utils.card_list_store import card_store
from utils.view_utils.pitcher_ratings_frame import PitcherRatingsFrame
from utils.view_utils.pitcher_individual_stats_frame import PitcherIndividualStatsFrame
from utils.view_utils.league_pitching_stats_frame import LeaguePitchingStatsFrame
from utils.view_utils.pitcher_stat_plot_frame import PitcherStatPlotFrame


class PitcherInfoView(ctk.CTkToplevel):
    """Class for viewing individual pitcher data."""

    def __init__(self, cid_value, file_path, team=None):
        """Initialize the pitcher view."""
        super().__init__()

        card_store.load_card_list()

        self.title('Pitcher Info')
        self.height = settings_module['FileProcessor']['height']
        self.width = settings_module['FileProcessor']['width']
        self.header_footer_height = int(self.height * 0.1)
        self.passed_team = team
        print("Passed team: ", self.passed_team)

        self.geometry(f'{self.width}x{self.height}')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)
        self.header_frame = Header(
            self,
            height=self.header_footer_height,
            width=self.width,
            title=f'Pitcher Info for {cid_value}',
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky='nsew',
        )

        self.pitcher_ratings_frame = PitcherRatingsFrame(
            self,
            cid_value=cid_value,
        )
        self.pitcher_ratings_frame.grid(
            row=1,
            column=0,
            sticky='nsew',
        )

        self.pitcher_stats_frame_overall = PitcherIndividualStatsFrame(
            self,
            cid_value=cid_value,
        )
        self.pitcher_stats_frame_overall.grid(
            row=1,
            column=1,
            sticky='nsew',
        )

        self.pitcher_stats_frame_team = PitcherIndividualStatsFrame(
            self,
            cid_value=cid_value,
            team=self.passed_team,
        )
        self.pitcher_stats_frame_team.grid(
            row=1,
            column=2,
            sticky='nsew',
        )

        self.league_pitching_stats_frame = LeaguePitchingStatsFrame(
            self,
        )
        self.league_pitching_stats_frame.grid(
            row=1,
            column=3,
            sticky='nsew',
        )

        self.pitcher_stats_plot_frame = PitcherStatPlotFrame(
            self
        )
        self.pitcher_stats_plot_frame.grid(
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

        show_and_release_topmost()
