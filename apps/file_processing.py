import tkinter as tk
from pathlib import Path
from tkinter import ttk
import customtkinter as ctk
from utils.load_settings import load_settings
from utils.file_selector import open_file

"""The file processing app will be used to take raw data from OOTP Baseball and convert it into a format
    useable by the rest of the applications."""


class FileProcessor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.settings = load_settings()


        self.title(f"{self.settings['FileProcessor']['title']}")
        self.geometry(f"{self.settings['MainWindow']['width']}x{self.settings['MainWindow']['height']}")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        header_footer_height = int(int(self.settings['MainWindow']['height']) * .1)

        self.header_frame = ctk.CTkFrame(self, height=header_footer_height, width=int(self.settings['MainWindow']['width']))
        self.header_frame.grid(column=0, row=0, padx=10, pady=10, sticky='new')

        self.footer_frame =ctk.CTkFrame(self, height=header_footer_height, width=int(self.settings['MainWindow']['width']))
        self.footer_frame.grid(column=0, row=2, padx=10, pady=10, sticky='sew')






if __name__ == '__main__':
    app = FileProcessor()
    app.mainloop()


