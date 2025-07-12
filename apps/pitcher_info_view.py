"""View for individual pitcher data."""
import customtkinter as ctk
from utils.config_utils.settings import settings as settings_module
from utils.view_utils.header_footer_frame import Header, Footer


class PitcherInfoView(ctk.CTkToplevel):
    """Class for viewing individual pitcher data."""

    def __init__(self, cid_value, file_path, selected_team=None):
        """Initialize the pitcher view."""
        super().__init__()

        self.title('Pitcher Info')
        self.height = settings_module['FileProcessor']['height']
        self.width = settings_module['FileProcessor']['width']
        self.header_footer_height = int(self.height * 0.1)

        self.geometry(f'{self.width}x{self.height}')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)
        self.header_frame = Header(
            self,
            height=self.header_footer_height,
            width=self.width,
            title=f'Pitcher Info for {cid_value}',
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky='nsew',
        )

        self.footer_frame = Footer(
            self,
            height=self.header_footer_height,
            width=self.width,
        )
        self.footer_frame.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky='nsew',
        )

        def show_and_release_topmost():
            """Lift window, set topmost and then release safely."""
            if not self.winfo_exists():
                return

            try:
                self.lift()
                self.attributes("-topmost", True)
            except Exception():
                return

            def release():
                if self.winfo_exists():
                    try:
                        self.attributes("-topmost", False)
                    except Exception:
                        pass

            self.after(100, release)

        show_and_release_topmost()
