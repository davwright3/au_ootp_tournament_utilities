"""App for viewing the basic tournament stats."""
import customtkinter as ctk
from utils import settings as settings_module
from utils.header_footer import Header, Footer

class BasicStatsView(ctk.CTkToplevel):
    """Initialize basic stats view.

    Uses CTKTopLevel to create the basic
    tournament stats viewer.
    """

    def __init__(self):
        """Initialize the app."""
        super().__init__()

        page_settings = settings_module.settings
        # Initialize the target file
        self.initial_target_file = None

        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = int(int(self.width) * .9)
        self.initial_target_dir = page_settings['InitialFileDirs']['initial_target_folder']
        header_footer_height = int(int(self.height) * .1)

        self.title = 'Basic Stats View'
        self.geometry(f"{self.width}x{self.height}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

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

        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width= int(self.frame_width)
        )
        self.footer_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')


        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)

