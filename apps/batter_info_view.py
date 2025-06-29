"""App for viewing individual player level data"""
import customtkinter as ctk
from utils.config_utils.settings import settings as settings_module


class BatterInfoView(ctk.CTkToplevel):
    """TopLevel view for BatterInfo.

    Uses CTK TopLevel to create a new window for viewing
    individual player level data.
    """

    def __init__(self, cid, filepath=None):
        super().__init__()

        self.title(f'Details for Card ID: {cid}')
        self.height = settings_module['FileProcessor']['height']
        self.width = settings_module['FileProcessor']['width']
        self.geometry(f'{self.width}x{self.height}')



        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)
        self.after(10, release_topmost)






