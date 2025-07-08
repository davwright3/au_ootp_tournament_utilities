"""Module to view basic team stats and results."""
import customtkinter as ctk
from utils.config_utils import settings as settings_module
from utils.file_utils.handle_select_file import handle_select_file
from utils.data_utils.get_team_list import get_team_list
from utils.stats_utils.display_basic_team_stats import display_basic_team_stats
from utils.view_utils.batter_stat_select_frame import BatterStatSelectFrame
from utils.view_utils.pitcher_stat_select_frame import PitcherStatSelectFrame
import pandas as pd

from utils.view_utils.all_player_data_view_frame import TreeviewTableFrame
from utils.view_utils.header_footer_frame import Header, Footer


class BasicTeamStatsView(ctk.CTkToplevel):
    """Initialize and format the application."""

    def __init__(self):
        """Initialize the basic team stats view."""
        super().__init__()

        page_settings = settings_module.settings
        # Initialize the target file
        self.target_file = None
        self.stats_df = pd.DataFrame()
        self.team_list = ["No teams loaded"]
        self.selected_team = ctk.StringVar(value="No teams loaded")

        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = int(int(self.width) * .9)
        self.initial_target_dir = (
            page_settings['InitialFileDirs']['initial_target_folder'])
        header_footer_height = int(int(self.height) * .1)

        self.title = "Basic Team Stats"
        self.geometry(f"{self.width}x{self.height}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        self.header_frame = Header(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
            title=self.title
        )
        self.header_frame.grid(
            row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew'
        )

        self.file_select_frame = ctk.CTkFrame(
            self
        )
        self.file_select_frame.grid(
            row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew'
        )

        self.data_view_frame = TreeviewTableFrame(self)
        self.data_view_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.menu_frame = ctk.CTkFrame(
            self
        )
        self.menu_frame.grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width=int(self.frame_width)
        )
        self.footer_frame.grid(
            row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew'
        )

        # Create the data for the frames
        self.file_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select File",
            command=self.select_file
        )
        self.file_select_button.grid(
            row=0, column=0, padx=10, pady=10, sticky='nsew'
        )

        self.file_select_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No file selected"
        )
        self.file_select_label.grid(
            row=0, column=1, padx=10, pady=10, sticky='nsew'
        )

        self.generate_team_list_button = ctk.CTkButton(
            self.file_select_frame,
            command=self.generate_team_list,
            text="Get Team List"
        )
        self.generate_team_list_button.grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.team_dropdown = ctk.CTkComboBox(
            self.file_select_frame,
            values=self.team_list,
            variable=self.selected_team
        )
        self.team_dropdown.set("No teams loaded")
        self.team_dropdown.grid(
            row=0,
            column=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.batting_stats_button = ctk.CTkButton(
            self.menu_frame,
            text="Display Stats",
            command=self.get_stats_to_display
        )
        self.batting_stats_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.batter_stat_select_frame = BatterStatSelectFrame(
            self.menu_frame
        )
        self.batter_stat_select_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.pitcher_stat_select_frame = PitcherStatSelectFrame(
            self.menu_frame
        )
        self.pitcher_stat_select_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        # self.lift()
        # self.focus_force()
        # self.attributes("-topmost", True)
        #
        # def release_topmost():
        #     self.attributes("-topmost", False)
        #
        # # self.after(10, release_topmost)
        # self.after(100, lambda: self.winfo_exists() and self.attributes("-topmost", False))

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


    def select_file(self):
        """Select new csv for processing."""
        selected = handle_select_file(self, self.initial_target_dir)
        if selected:
            self.target_file = selected
            self.file_select_label.configure(
                text=f"Selected: {selected.split('/')[-1]}"
            )
        else:
            self.log_message("File selection cancelled")

    def generate_team_list(self):
        """Process file for team list."""
        df = pd.read_csv(self.target_file)
        self.set_team_list(df)
        del df

    def set_team_list(self, df):
        """Create list for team list."""
        self.team_list = get_team_list(df)
        self.team_dropdown.configure(values=self.team_list)
        del df

    def get_stats_to_display(self):
        """Process file and display stats."""
        selected_batting_stats = self.batter_stat_select_frame.get_active_stats() # noqa:
        selected_pitching_stats = self.pitcher_stat_select_frame.get_active_stats() # noqa:
        df = display_basic_team_stats(
            pd.read_csv(self.target_file),
            selected_batting_stats,
            selected_pitching_stats
        )
        self.data_view_frame.load_dataframe(
            df,
            passed_team=self.selected_team.get()
        )
        del df

    def log_message(self, message):
        """Update message label."""
        self.file_select_label.configure(text=message)
