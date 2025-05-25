import tkinter as tk
import sys
import os
from pathlib import Path
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import load_settings as _settings

"""The file processing app will be used to take raw data from OOTP Baseball and convert it into a format
    useable by the rest of the applications."""

class FileProcessor(tk.Tk):
    def __init__(self):
        super().__init__()

        #Load json settings file
        self.settings = _settings.load_settings()

        #Set element heights from the settings
        self.height = int(self.settings['FileProcessor']['height'])
        self.width = int(self.settings['FileProcessor']['width'])
        self.frame_width = self.width * .9

        #Title and window size from the settings
        self.title(f"{self.settings['FileProcessor']['title']}")
        self.geometry(f"{self.width}x{self.height}")

        #Variables for grid Configurations
        self.grid_columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        header_footer_height = int(int(self.height) * .1)

        #Set up the frames
        self.header_frame = ctk.CTkFrame(self, height=header_footer_height, width=int(self.frame_width))
        self.header_frame.grid(column=0, row=0, padx=10, pady=10, sticky='n')

        self.file_select_frame = ctk.CTkFrame(self, height=header_footer_height, width=int(self.frame_width))
        self.file_select_frame.grid(column=0, row=1, padx=10, pady=10, sticky='n')

        self.main_frame = ctk.CTkFrame(self, corner_radius=5, width=int(self.frame_width))
        self.main_frame.grid(column=0, row=2, padx=10, pady=10, sticky='ns')

        self.footer_frame =ctk.CTkFrame(self, height=header_footer_height, width=int(self.frame_width))
        self.footer_frame.grid(column=0, row=3, padx=10, pady=10, sticky='n')






if __name__ == '__main__':
    app = FileProcessor()
    app.mainloop()


