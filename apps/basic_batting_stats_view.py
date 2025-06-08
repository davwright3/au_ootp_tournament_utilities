"""App for viewing the basic tournament stats."""
import customtkinter as ctk
from utils.config_utils import settings as settings_module
from utils.view_utils.header_footer import Header, Footer
from utils.view_utils.data_view_frame import TreeviewTableFrame
from utils.file_utils.handle_select_file import handle_select_file
from utils.stats_utils.calc_basic_batting_stats import calc_basic_stats
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
        self.initial_target_dir = page_settings['InitialFileDirs']['initial_target_folder']
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
            width= int(self.frame_width),
            title="Basic Stats View"
        )
        self.header_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

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
        self.data_view_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

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
            width= int(self.frame_width)
        )
        self.footer_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        self.file_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select File",
            command=self.select_file
        )
        self.file_select_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.file_select_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No File Selected")
        self.file_select_label.grid(row=0, column=1, padx=10, pady=10)

        self.process_button = ctk.CTkButton(
            self.file_select_frame,
            text="Process",
            command=self.process_file
        )
        self.process_button.grid(row=0, column=2, padx=10, pady=10)

        self.plate_app_label = ctk.CTkLabel(
            self.menu_frame,
            text="Min PA"
        )
        self.plate_app_label.grid(row=0, column=0, padx=10, pady=10)

        self.plate_app_entry = ctk.CTkEntry(
            self.menu_frame
        )
        self.plate_app_entry.grid(row=1, column=0, padx=10, pady=10)


        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)


    def select_file(self):
        self.target_file = handle_select_file(self, self.initial_target_dir)


    def process_file(self):
        if not self.target_file:
            self.log_message("No file selected")
            return

        try:
            try:
                min_pa = int(self.plate_app_entry.get())
            except (ValueError, TypeError):
                min_pa = 600

            df=calc_basic_stats(pd.read_csv(self.target_file), min_pa)
            self.data_view_frame.load_dataframe(df)
            self.update_idletasks()
            self.log_message("Data loaded")
        except Exception as e:
            self.log_message(f"Error loading {self.target_file}: {e}")


    def log_message(self, message):
        self.file_select_label.configure(text=message)