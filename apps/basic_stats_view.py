"""App for viewing the basic tournament stats."""
import customtkinter as ctk
from utils import settings as settings_module

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
        self.frame_width = int(self.width * .9)
        self.initial_target_dir = page_settings['InitialFileDirs']['data']

        self.title = 'Basic Stats View'
        self.geometry(f"{self.width}x{self.height}")




        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)

