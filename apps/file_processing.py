"""App for processing raw files."""
import os.path
import tkinter as tk
import customtkinter as ctk
from utils.settings import settings
from utils.header_footer import Header, Footer
from utils.file_selector import open_file
from utils.folder_selector import select_folder


class FileProcessor(tk.Tk):
    """Load module for processing raw files."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()

        # Set element heights from the settings
        self.height = int(settings['FileProcessor']['height'])
        self.width = int(settings['FileProcessor']['width'])
        self.frame_width = self.width * .9
        self.initial_target_dir = settings['InitialFileDirs']['target']
        self.initial_data_dir = settings['InitialFileDirs']['data']

        # Title and window size from the settings
        self.title(f"{settings['FileProcessor']['title']}")
        self.geometry(f"{self.width}x{self.height}")

        # Variables for grid Configurations
        self.grid_columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        header_footer_height = int(int(self.height) * .1)

        # Set up the frames
        # Header frame
        self.header_frame = Header(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
            title="File Processing Tool"
        )
        self.header_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        # File/folder selection frame
        self.file_select_frame = ctk.CTkFrame(
            self, height=header_footer_height, width=int(self.frame_width)
        )
        self.file_select_frame.grid(
            column=0, row=1, padx=10, pady=10, sticky='new'
        )
        self.file_select_frame.columnconfigure(0, weight=0)
        self.file_select_frame.columnconfigure(1, weight=0)
        self.file_select_frame.columnconfigure(2, weight=1)
        self.file_select_frame.columnconfigure(3, weight=0)
        self.file_select_frame.rowconfigure(0, weight=1)
        self.file_select_frame.rowconfigure(1, weight=1)

        # Main frame
        self.main_frame = ctk.CTkFrame(
            self, corner_radius=5, width=int(self.frame_width)
        )
        self.main_frame.grid(
            column=0, row=2, padx=10, pady=10, sticky='nsew'
        )

        # Footer frame
        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width=int(self.frame_width)
        )
        self.footer_frame.grid(
            column=0, row=3, padx=10, pady=10, sticky='ew')

        # Set up the data for the file/folder selection frame
        self.target_file_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select target file",
            command=self.select_file
        )
        self.target_file_select_button.grid(column=0, row=0)

        self.target_file_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No file selected"
        )
        self.target_file_label.grid(column=1, row=0)

        self.data_folder_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select data folder",
            command=self.select_folder_handler
        )
        self.data_folder_select_button.grid(column=0, row=1)

        self.data_folder_select_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No data folder selected"
        )
        self.data_folder_select_label.grid(column=1, row=1)

        self.process_files_button = ctk.CTkButton(
            self.file_select_frame,
            text="Process files",
            command=self.process_files
        )
        self.process_files_button.grid(column=3, row=1)

    def select_file(self):
        """Open select target file dialog."""
        path = self.initial_target_dir.strip().replace("\\", "/")
        if os.path.isdir(path):
            file = open_file(parent=self, initial_dir=self.initial_target_dir)
            if file:
                self.target_file_label.configure(text=file.name)
        else:
            print("Invalid start directory")
            self.target_file_label.configure(text="Invalid start directory")

    def select_folder_handler(self):
        """Open select data folder dialog."""
        data_directory = select_folder(
            parent=self,
            initial_dir=self.initial_data_dir)
        if data_directory:
            self.data_folder_select_label.configure(text=data_directory)

    def process_files(self):
        """Process files into the ready CSV."""

    def add_new_file(self):
        """Use template file to create a new file in the target directory."""


if __name__ == '__main__':
    app = FileProcessor()
    app.mainloop()
