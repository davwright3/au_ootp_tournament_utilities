"""App for viewing the basic tournament stats."""
import customtkinter as ctk
from utils.config_utils import settings as settings_module
from utils.data_utils.get_team_list import get_team_list
from utils.view_utils.header_footer_frame import Header, Footer
from utils.view_utils.all_player_data_view_frame import TreeviewTableFrame
from utils.file_utils.handle_select_file import handle_select_file
from utils.stats_utils.display_basic_player_batting_stats import (
    display_basic_batting_stats)
from utils.interface_utils.pos_select_button import CustomPositionButton
from utils.view_utils.batter_stat_select_frame import BatterStatSelectFrame
from utils.view_utils.card_value_select_frame import CardValueSelectFrame
from utils.view_utils.general_stat_select_frame import GeneralStatSelectFrame
from utils.data_utils.data_store import data_store
from utils.data_utils.league_batting_stats import league_stats
import pandas as pd


class BasicStatsView(ctk.CTkToplevel):
    """Initialize basic stats view.

    Uses CTKTopLevel to create the basic
    tournament stats viewer.
    """

    data = pd.DataFrame()

    def __init__(self):
        """Initialize the app."""
        super().__init__()

        page_settings = settings_module.settings
        # Initialize the target file
        self.target_file = None
        self.stats_df = pd.DataFrame(['No file selected'])
        self.variant_select = ctk.BooleanVar(value=False)
        self.batter_side_select = ctk.StringVar(value='Any')
        self.batter_search_name = None
        self.role = 'batter'
        self.team_list = ['No teams loaded']
        self.selected_team = ctk.StringVar(value="No teams loaded")

        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = int(int(self.width) * .9)
        self.initial_target_dir = (
            page_settings['InitialFileDirs']['initial_target_folder'])
        header_footer_height = int(int(self.height) * .1)

        self.title = 'Basic Stats View'
        self.geometry(f"{self.width}x{self.height}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # Set up the frames for the page
        self.header_frame = Header(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
            title=self.title
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.file_select_frame = ctk.CTkFrame(
            self
        )
        self.file_select_frame.grid(
            row=1,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='new')

        self.data_view_frame = TreeviewTableFrame(self)
        self.data_view_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky='nsew')

        self.menu_frame = ctk.CTkFrame(
            self
        )
        self.menu_frame.grid(
            row=2,
            column=2,
            padx=20,
            pady=10,
            sticky='nsew'
        )
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
        self.menu_frame.rowconfigure(10, weight=0)
        self.menu_frame.rowconfigure(11, weight=0)
        self.menu_frame.rowconfigure(12, weight=0)
        self.menu_frame.rowconfigure(13, weight=0)
        self.menu_frame.rowconfigure(14, weight=0)
        self.menu_frame.rowconfigure(15, weight=1)

        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.columnconfigure(1, weight=1)
        self.menu_frame.columnconfigure(2, weight=1)

        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width=int(self.frame_width)
        )
        self.footer_frame.grid(
            row=3,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        # Data for the page
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
            sticky='w'
        )

        self.file_select_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No File Selected"
        )
        self.file_select_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
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

        # Menu frame buttons and entries
        self.batter_search_label = ctk.CTkLabel(
            self.menu_frame,
            text="Batter Search"
        )
        self.batter_search_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.batter_search_entry = ctk.CTkEntry(
            self.menu_frame,
        )
        self.batter_search_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        self.plate_app_label = ctk.CTkLabel(
            self.menu_frame,
            text="Min PA"
        )
        self.plate_app_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.plate_app_entry = ctk.CTkEntry(
            self.menu_frame
        )
        self.plate_app_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        self.variant_checkbox = ctk.CTkCheckBox(
            self.menu_frame,
            text="Split Variant",
            variable=self.variant_select,
        )
        self.variant_checkbox.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        self.batter_side_label = ctk.CTkLabel(
            self.menu_frame,
            text="Batter Side"
        )
        self.batter_side_label.grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.batter_side_checkbox = ctk.CTkComboBox(
            self.menu_frame,
            values=['R', 'L', 'S', 'Any'],
            command=self.set_batter_side,
            variable=self.batter_side_select,
            border_color="black",
            button_color="violet",
            button_hover_color="darkviolet",
        )
        self.batter_side_checkbox.set('Any')
        self.batter_side_checkbox.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.catcher_button = CustomPositionButton(
            self.menu_frame,
            width=50,
            text="C",
            command=lambda: (self.run_position_file(pos='LearnC'),
                             self.log_message("Catchers"))
        )
        self.catcher_button.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
        )

        self.first_base_button = CustomPositionButton(
            self.menu_frame,
            text="1B",
            width=50,
            command=lambda: (self.run_position_file(pos='Learn1B'),
                             self.log_message("First Base"))
        )
        self.first_base_button.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
        )

        self.second_base_button = CustomPositionButton(
            self.menu_frame,
            text="2B",
            width=50,
            command=lambda: (self.run_position_file(pos='Learn2B'),
                             self.log_message("Second Base"))
        )
        self.second_base_button.grid(
            row=4,
            column=2,
            padx=5,
            pady=5,
        )

        self.third_base_button = CustomPositionButton(
            self.menu_frame,
            text="3B",
            width=50,
            command=lambda: (self.run_position_file(pos='Learn3B'),
                             self.log_message("Third Base"))
        )
        self.third_base_button.grid(
            row=5,
            column=0,
            padx=5,
            pady=5
        )

        self.shortstop_button = CustomPositionButton(
            self.menu_frame,
            text="SS",
            width=50,
            command=lambda: (self.run_position_file(pos='LearnSS'),
                             self.log_message("Shortstop"))
        )
        self.shortstop_button.grid(
            row=5,
            column=1,
            padx=5,
            pady=5
        )

        self.left_field_button = CustomPositionButton(
            self.menu_frame,
            text="LF",
            width=50,
            command=lambda: (self.run_position_file(pos='LearnLF'),
                             self.log_message("Left Field"))
        )
        self.left_field_button.grid(
            row=5,
            column=2,
            padx=5,
            pady=5
        )

        self.center_field_button = CustomPositionButton(
            self.menu_frame,
            text="CF",
            width=50,
            command=lambda: (self.run_position_file(pos='LearnCF'),
                             self.log_message("Center Field"))
        )
        self.center_field_button.grid(
            row=6,
            column=0,
            padx=5,
            pady=5
        )

        self.right_field_button = CustomPositionButton(
            self.menu_frame,
            text="RF",
            width=50,
            command=lambda: (self.run_position_file(pos='LearnRF'),
                             self.log_message("Right Field"))
        )
        self.right_field_button.grid(
            row=6,
            column=1,
            padx=5,
            pady=5
        )

        self.all_batters_button = CustomPositionButton(
            self.menu_frame,
            text="ALL",
            width=50,
            command=lambda: (self.run_position_file(pos=None),
                             self.log_message("All Batters"))
        )
        self.all_batters_button.grid(
            row=6,
            column=2,
            padx=5,
            pady=5
        )

        self.batter_stat_select_frame = BatterStatSelectFrame(
            self.menu_frame
        )
        self.batter_stat_select_frame.grid(
            row=7,
            column=0,
            columnspan=3,
            padx=5,
            pady=5
        )

        self.card_value_frame = CardValueSelectFrame(
            self.menu_frame
        )
        self.card_value_frame.grid(
            row=8,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.general_stats_select_frame = GeneralStatSelectFrame(
            self.menu_frame
        )
        self.general_stats_select_frame.grid(
            row=9,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky='nsew'
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

    def select_file(self):
        """Select new csv for processing."""
        selected = handle_select_file(self, self.initial_target_dir)
        if selected:
            self.target_file = selected
            self.file_select_label.configure(
                text=f"Selected: {selected.split('/')[-1]}"
            )
            self.load_data_to_store()
        else:
            self.log_message("File selection cancelled")

    def run_position_file(self, pos=None):
        """Run the calculations for selected position."""
        if not self.target_file:
            self.log_message("No file selected")
            return

        try:
            try:
                min_pa = int(self.plate_app_entry.get())
            except (ValueError, TypeError):
                min_pa = 600

            if len(self.batter_search_entry.get()) != 0:
                self.batter_search_name = self.batter_search_entry.get()
            else:
                self.batter_search_name = None

            stats_to_view = self.get_active_stats()
            general_stats_to_view = self.get_active_general_stats()
            min_value, max_value = self.card_value_frame.get_min_max_values()
            try:
                min_value = int(min_value)
                max_value = int(max_value)
            except (ValueError, TypeError):
                min_value = 40
                max_value = 105

            df = display_basic_batting_stats(
                min_pa,
                pos,
                variant_split=self.variant_select.get(),
                batter_side=self.batter_side_select.get(),
                batter_name=self.batter_search_name,
                stats_to_view=stats_to_view,
                general_stats_to_view=general_stats_to_view,
                min_value=min_value,
                max_value=max_value,
            )

            self.data_view_frame.load_dataframe(
                df,
                passed_team=self.selected_team.get()
            )
            self.update_idletasks()
            self.log_message("Data loaded")
        except Exception as e:
            self.log_message(f"Error loading {self.target_file}: {e}")

    def set_batter_side(self, choice):
        """Set batter handedness selection."""
        self.batter_side_select.set(choice)

    def log_message(self, message):
        """Update message label."""
        self.file_select_label.configure(text=message)

    def get_active_stats(self):
        """Get the list of selected stats."""
        return self.batter_stat_select_frame.get_active_stats()

    def get_active_general_stats(self):
        """Get the list of selected general stats."""
        return self.general_stats_select_frame.get_selected_general_stats()

    def load_data_to_store(self):
        """Process file for team list."""
        if not self.target_file:
            print("No file selected")
            return

        data_store.load_data(self.target_file)
        df = data_store.get_data()
        self.set_team_list(df)
        league_stats.set_league_stats()

    def set_team_list(self, df):
        """Create list for team list."""
        self.team_list = get_team_list(df)
        self.team_dropdown.configure(values=self.team_list)
        del df
