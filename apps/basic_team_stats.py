"""Module to view basic team stats and results"""
import customtkinter as ctk
from utils.config_utils import settings as settings_module
import pandas as pd

from utils.view_utils.header_footer import Header, Footer


class BasicTeamStatsView(ctk.CTkToplevel):
    """Initialize and format the application"""

    def __init__(self):
        super().__init__()

        page_settings = settings_module.settings
        # Initialize the target file
        self.target_file = None
        self.stats_df = pd.DataFrame()
        self.team_list = []

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

        self.main_frame = ctk.CTkFrame(
            self
        )
        self.main_frame.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nsew'
        )


        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width=int(self.frame_width)
        )
        self.footer_frame.grid(
            row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew'
        )




        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)

        self.after(10, release_topmost)


