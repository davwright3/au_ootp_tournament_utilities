"""App for viewing basic pitching stats."""
import customtkinter as ctk
import pandas as pd
from utils.config_utils import settings as settings_module
from utils.stats_utils.display_basic_player_pitching_stats import (
    display_basic_pitching_stats
)
from utils.view_utils.header_footer_frame import Header, Footer
from utils.view_utils.data_view_frame import TreeviewTableFrame
from utils.file_utils.handle_select_file import handle_select_file
from utils.view_utils.pitcher_stat_select_frame import PitcherStatSelectFrame
from utils.view_utils.card_value_select_frame import CardValueSelectFrame


class BasicPitchingStatsView(ctk.CTkToplevel):
    """Initialize basic pitching stats view."""

    data = pd.DataFrame()

    def __init__(self):
        """Initialize the stats view app."""
        super().__init__()
        """Initialize the basic pitching stats view."""

        page_settings = settings_module.settings

        self.target_file = None
        self.df = pd.DataFrame(["No file selected"])
        self.min_ip = 200
        self.inning_split = 4
        self.variant_select = ctk.BooleanVar(value=False)
        self.pitching_side_checkbox = ctk.StringVar(value='Any')
        self.player_search_name = None

        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = int(self.width*.9)
        self.initial_target_dir = (
            page_settings['InitialFileDirs']['initial_target_folder']
        )
        self.header_footer_height = int(self.height*.1)

        self.title = "Basic Pitching Stats"
        self.geometry(f"{self.width}x{self.height}")

        # Set up the frames
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        self.header_frame = Header(
            self,
            height=self.header_footer_height,
            width=self.frame_width,
            title="Basic Pitching Stats")
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.file_select_frame = ctk.CTkFrame(
            self,

        )
        self.file_select_frame.grid(
            row=1,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.data_view_frame = TreeviewTableFrame(self)
        self.data_view_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.menu_frame = ctk.CTkFrame(
            self
        )
        self.menu_frame.grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.menu_frame.columnconfigure(0, weight=0)
        self.menu_frame.columnconfigure(1, weight=1)
        self.menu_frame.columnconfigure(2, weight=0)

        self.menu_frame.rowconfigure(0, weight=0)
        self.menu_frame.rowconfigure(1, weight=0)
        self.menu_frame.rowconfigure(2, weight=0)
        self.menu_frame.rowconfigure(3, weight=0)
        self.menu_frame.rowconfigure(4, weight=0)
        self.menu_frame.rowconfigure(5, weight=0)
        self.menu_frame.rowconfigure(6, weight=0)
        self.menu_frame.rowconfigure(7, weight=0)
        self.menu_frame.rowconfigure(8, weight=0)
        self.menu_frame.rowconfigure(9, weight=0)
        self.menu_frame.rowconfigure(10, weight=1)

        self.footer_frame = Footer(
            self,
            height=self.header_footer_height,
            width=self.frame_width
        )
        self.footer_frame.grid(
            row=3,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # Data to be entered into the frames
        self.file_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select File",
            command=self.select_file
        )
        self.file_select_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.file_select_label = ctk.CTkLabel(
            self.file_select_frame,
            text="Select File"
        )
        self.file_select_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="w",
        )

        self.process_button = ctk.CTkButton(
            self.file_select_frame,
            text="Process Data",
            command=self.run_pitcher_file
        )
        self.process_button.grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Menu frame data
        self.player_search_label = ctk.CTkLabel(
            self.menu_frame,
            text="Player Search"
        )
        self.player_search_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.player_search_entry = ctk.CTkEntry(
            self.menu_frame,
        )
        self.player_search_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
        )

        self.min_innings_label = ctk.CTkLabel(
            self.menu_frame,
            text="Min IP"
        )
        self.min_innings_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew",
        )

        self.min_innings_input = ctk.CTkEntry(
            self.menu_frame,
        )
        self.min_innings_input.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew",
        )

        self.innings_split_label = ctk.CTkLabel(
            self.menu_frame,
            text="SP/RP Split"
        )
        self.innings_split_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.innings_split_input = ctk.CTkEntry(
            self.menu_frame
        )
        self.innings_split_input.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.variant_checkbox = ctk.CTkCheckBox(
            self.menu_frame,
            text="Split Variants",
            variable=self.variant_select
        )
        self.variant_checkbox.grid(
            row=3,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.pitching_side_label = ctk.CTkLabel(
            self.menu_frame,
            text="Pitching Side"
        )
        self.pitching_side_label.grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.pitching_side_checkbox = ctk.CTkComboBox(
            self.menu_frame,
            values=['L', 'R', 'Any'],
            command=self.set_pitcher_side,
            variable=self.pitching_side_checkbox,
            border_color='black',
            button_color='violet',
            button_hover_color='darkviolet'
        )
        self.pitching_side_checkbox.set('Any')
        self.pitching_side_checkbox.grid(
            row=4,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.starting_pitchers_button = ctk.CTkButton(
            self.menu_frame,
            text="Starting Pitchers",
            command=lambda: self.run_pitcher_file(pos=1)
        )
        self.starting_pitchers_button.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
        )

        self.relief_pitchers_button = ctk.CTkButton(
            self.menu_frame,
            text="Relief Pitchers",
            command=lambda: self.run_pitcher_file(pos=2)
        )
        self.relief_pitchers_button.grid(
            row=6,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
        )

        self.all_pitchers_button = ctk.CTkButton(
            self.menu_frame,
            text="All Pitchers",
            command=self.run_pitcher_file
        )
        self.all_pitchers_button.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

        self.pitching_stats_select_frame = PitcherStatSelectFrame(
            self.menu_frame
        )
        self.pitching_stats_select_frame.grid(
            row=8,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.card_value_select_frame = CardValueSelectFrame(
            self.menu_frame,
        )
        self.card_value_select_frame.grid(
            row=9,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)

    def select_file(self):
        """Select csv file for processing."""
        selected = handle_select_file(self, self.initial_target_dir)
        if selected:
            self.target_file = selected
            self.file_select_label.configure(
                text=f"Selected: {selected.split('/')[-1]}"
            )
        else:
            self.log_message("File selection cancelled")

    def run_pitcher_file(self, pos=None):
        """Run calculations script for pitching stats."""
        if not self.target_file:
            self.log_message("No file selected")
            return

        try:
            self.min_ip = int(self.min_innings_input.get())
        except ValueError:
            self.min_ip = 200

        try:
            self.inning_split = int(self.innings_split_input.get())
        except ValueError:
            self.inning_split = 4

        if len(self.player_search_entry.get()) != 0:
            self.player_search_name = self.player_search_entry.get()
        else:
            self.player_search_name = None

        pitching_stats_to_view = self.get_pitching_stats_to_view()
        min_value, max_value = self.card_value_select_frame.get_min_max_values()

        try:
            min_value = int(min_value)
            max_value = int(max_value)
        except ValueError:
            min_value = 40
            max_value = 105

        df = display_basic_pitching_stats(
            pd.read_csv(self.target_file),
            self.min_ip,
            role=pos,
            inning_split=self.inning_split,
            variant_split=self.variant_select.get(),
            pitching_side=self.pitching_side_checkbox.get(),
            player_name=self.player_search_name,
            pitching_stats_to_view=pitching_stats_to_view,
            min_value=min_value,
            max_value=max_value,
        )

        self.data_view_frame.load_dataframe(df)
        self.update_idletasks()
        self.log_message("Pitcher file loaded")

    def set_pitcher_side(self, choice):
        """Set pitcher handedness selection."""
        self.pitching_side_checkbox.set(choice)

    def log_message(self, message):
        """Log status update messages."""
        self.file_select_label.configure(text=message)

    def get_pitching_stats_to_view(self):
        """Get list of selected pitching stats."""
        return self.pitching_stats_select_frame.get_active_stats()
