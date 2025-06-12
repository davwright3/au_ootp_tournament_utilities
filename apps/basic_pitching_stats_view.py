import customtkinter as ctk
import pandas as pd
from utils.config_utils import settings as settings_module
from utils.stats_utils.calc_basic_pitching_stats import calc_basic_pitching_stats
from utils.view_utils.header_footer import Header, Footer
from utils.view_utils.data_view_frame import TreeviewTableFrame
from utils.file_utils.handle_select_file import handle_select_file


class BasicPitchingStatsView(ctk.CTkToplevel):
    """Initialize basic pitching stats view."""

    data = pd.DataFrame()

    def __init__(self):
        """Initialize the stats view app"""

        super().__init__()
        """Initialize the basic pitching stats view."""

        page_settings = settings_module.settings

        self.target_file = None
        self.df = pd.DataFrame(["No file selected"])

        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = int(self.width*.9)
        self.initial_target_dir = page_settings['InitialFileDirs']['initial_target_folder']
        self.header_footer_height = int(self.height*.1)

        self.title = "Basic Pitching Stats"
        self.geometry(f"{self.width}x{self.height}")

        # Set up the frames
        self.grid_columnconfigure(0, weight=1)
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
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

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



        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)

    def select_file(self):
        selected = handle_select_file(self, self.initial_target_dir)
        if selected:
            self.target_file = selected
            self.file_select_label.configure(text=f"Selected: {selected.split('/')[-1]}")
        else:
            self.log_message("File selection cancelled")


    def run_pitcher_file(self):
        if not self.target_file:
            self.log_message("No file selected")
            return

        print("Running pitcher file")
        df = calc_basic_pitching_stats(pd.read_csv(self.target_file))

        self.data_view_frame.load_dataframe(df)
        self.update_idletasks()
        self.log_message("Pitcher file loaded")



    def log_message(self, message):
        self.file_select_label.configure(text=message)



