"""App for viewing the basic tournament stats."""
import customtkinter as ctk
from utils.config_utils import settings as settings_module
from utils.view_utils.header_footer import Header, Footer
from utils.view_utils.data_view_frame import TreeviewTableFrame
from utils.file_utils.handle_select_file import handle_select_file
from utils.stats_utils.calc_basic_batting_stats import calc_basic_batting_stats
from utils.interface_utils.pos_select_button import CustomPositionButton
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
            padx=10,
            pady=10,
            sticky='nsw'
        )
        self.menu_frame.rowconfigure(0, weight=1)
        self.menu_frame.rowconfigure(1, weight=1)
        self.menu_frame.rowconfigure(2, weight=1)
        self.menu_frame.rowconfigure(3, weight=1)
        self.menu_frame.rowconfigure(4, weight=1)
        self.menu_frame.rowconfigure(5, weight=1)
        self.menu_frame.rowconfigure(6, weight=1)
        self.menu_frame.rowconfigure(7, weight=1)
        self.menu_frame.rowconfigure(8, weight=1)
        self.menu_frame.rowconfigure(9, weight=1)
        self.menu_frame.rowconfigure(10, weight=1)

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
            text="No File Selected")
        self.file_select_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        self.process_button = ctk.CTkButton(
            self.file_select_frame,
            text="Process",
            command=self.run_position_file
        )
        self.process_button.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        self.plate_app_label = ctk.CTkLabel(
            self.menu_frame,
            text="Min PA"
        )
        self.plate_app_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.plate_app_entry = ctk.CTkEntry(
            self.menu_frame
        )
        self.plate_app_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.catcher_button = CustomPositionButton(
            self.menu_frame,
            text="Catcher",
            command=lambda: (self.run_position_file(pos='LearnC'),
                             self.log_message("Catchers"))
        )
        self.catcher_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        self.first_base_button = CustomPositionButton(
            self.menu_frame,
            text="First Base",
            command=lambda: (self.run_position_file(pos='Learn1B'),
                             self.log_message("First Base"))
        )
        self.first_base_button.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )

        self.second_base_button = CustomPositionButton(
            self.menu_frame,
            text="Second Base",
            command=lambda: (self.run_position_file(pos='Learn2B'),
                             self.log_message("Second Base"))
        )
        self.second_base_button.grid(
            row=4,
            column=0,
            padx=10,
            pady=10
        )

        self.third_base_button = CustomPositionButton(
            self.menu_frame,
            text="Third Base",
            command=lambda: (self.run_position_file(pos='Learn3B'),
                             self.log_message("Third Base"))
        )
        self.third_base_button.grid(
            row=5,
            column=0,
            padx=10,
            pady=10
        )

        self.shortstop_button = CustomPositionButton(
            self.menu_frame,
            text="Shortstop",
            command=lambda: (self.run_position_file(pos='LearnSS'),
                             self.log_message("Shortstop"))
        )
        self.shortstop_button.grid(
            row=6,
            column=0,
            padx=10,
            pady=10
        )

        self.left_field_button = CustomPositionButton(
            self.menu_frame,
            text="Left Field",
            command=lambda: (self.run_position_file(pos='LearnLF'),
                             self.log_message("Left Field"))
        )
        self.left_field_button.grid(
            row=7,
            column=0,
            padx=10,
            pady=10
        )

        self.center_field_button = CustomPositionButton(
            self.menu_frame,
            text="Center Field",
            command=lambda: (self.run_position_file(pos='LearnCF'),
                             self.log_message("Center Field"))
        )
        self.center_field_button.grid(
            row=8,
            column=0,
            padx=10,
            pady=10
        )

        self.right_field_button = CustomPositionButton(
            self.menu_frame,
            text="Right Field",
            command=lambda: (self.run_position_file(pos='LearnRF'),
                             self.log_message("Right Field"))
        )
        self.right_field_button.grid(
            row=9,
            column=0,
            padx=10,
            pady=10
        )

        self.all_batters_button = CustomPositionButton(
            self.menu_frame,
            text="Batters",
            command=lambda: (self.run_position_file(pos=None),
                             self.log_message("All Batters"))
        )
        self.all_batters_button.grid(
            row=10,
            column=0,
            padx=10,
            pady=10
        )

        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)

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

            df = calc_basic_batting_stats(
                pd.read_csv(self.target_file), min_pa, pos
            )

            self.data_view_frame.load_dataframe(df)
            self.update_idletasks()
            self.log_message("Data loaded")
        except Exception as e:
            self.log_message(f"Error loading {self.target_file}: {e}")

    def log_message(self, message):
        """Update message label."""
        self.file_select_label.configure(text=message)
