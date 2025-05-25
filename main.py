import sys

import customtkinter as ctk
import subprocess
import os
from utils.app_select_button import AppSelectButton
from PIL import Image
from utils.load_settings import load_settings
from utils.header_footer import Header, Footer


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme('themes/main_theme.json')

        # load settings from load_settings utility
        self.settings = load_settings()
        self.title(f"{self.settings['App']['title']}")

        self.height = self.settings['MainWindow']['height']
        self.width = self.settings['MainWindow']['width']
        self.geometry(
            f"{self.width}x{self.height}"
        )

        # Variables for page sizing
        self.frame_width = int(self.width) * .9
        header_footer_height = int(int(self.height)*.1)

        # Set grids for the main page
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Create header frame
        self.header_frame = Header(self, height=header_footer_height, width=int(self.frame_width))
        self.header_frame.grid(column=0, row=0, columnspan=3, padx=10, pady=10, sticky='new')

        self.header_frame.grid_columnconfigure(0, weight=1)

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=5, width=int(self.frame_width))
        self.main_frame.grid(column=0, row=1, columnspan=3, padx=10, sticky="nsew")

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

        # Create footer frame
        self.footer_frame = Footer(self, height=header_footer_height, width=int(self.frame_width))
        self.footer_frame.grid(column=0, row=2, columnspan=3, padx=10, pady=10, sticky='sew')

        # Main frame data
        self.file_processing_select_button = (
            AppSelectButton(
                self.main_frame,
                command=open_file_processing,
                text="File Processing")
        )
        self.file_processing_select_button.grid(
            column=0, row=0, padx=10, pady=10, sticky='nsew'
        )




"""
This method will open the file processing app in a new window


"""


def open_file_processing():
    subprocess.Popen([sys.executable, '-m', 'apps.file_processing'])


"""
This method will open the edit settings portion of the app

"""


def open_edit_settings():
    subprocess.Popen([sys.executable, '-m', "apps.update_settings"])


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
