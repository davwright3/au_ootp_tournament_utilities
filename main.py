"""This is the main menu opening for the program."""
import customtkinter as ctk
import sys

from apps.basic_stats_view import BasicStatsView
from utils.get_base_sys_path import get_base_sys_path

sys.path.insert(0, get_base_sys_path())
from utils.app_select_button import AppSelectButton
from utils.settings import settings, reload_settings
from utils.header_footer import Header, Footer
from apps.file_processing import FileProcessor


class MainApp(ctk.CTk):
    """This class opens and runs the main window."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        ctk.set_default_color_theme('blue')

        # load settings from load_settings utility
        self.title(settings['App']['title'])
        self.height = settings['MainWindow']['height']
        self.width = settings['MainWindow']['width']
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
        self.header_frame = Header(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
            title="Angered Unicorn's OOTP Tournament Utilities")
        self.header_frame.grid(
            column=0, row=0, columnspan=3, padx=10, pady=10, sticky='new'
        )

        self.header_frame.grid_columnconfigure(0, weight=1)

        # Create main frame
        self.main_frame = ctk.CTkFrame(
            self, corner_radius=5, width=int(self.frame_width)
        )
        self.main_frame.grid(
            column=0, row=1, columnspan=3, padx=10, sticky="nsew"
        )

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

        def on_settings_updated():
            reload_settings()
            self.settings = settings

        # Create footer frame
        self.footer_frame = Footer(
            self, height=header_footer_height,
            width=int(self.frame_width),
            on_settings_updated=on_settings_updated
        )
        self.footer_frame.grid(
            column=0, row=2, columnspan=3, padx=10, pady=10, sticky='sew'
        )

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

        self.basic_stats_view_button = (
            AppSelectButton(
                self.main_frame,
                command=open_basic_stats_view,
                text="Basic Stats View"

            )
        )
        self.basic_stats_view_button.grid(
            column=1, row=0, padx=10, pady=10, sticky='nsew'
        )


def open_file_processing():
    """Open the file processing app in a new window."""
    FileProcessor()


def open_basic_stats_view():
    """Open the basic stats view app in a new window."""
    BasicStatsView()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
