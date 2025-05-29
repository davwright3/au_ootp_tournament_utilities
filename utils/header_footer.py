"""Use on all apps to generate header and footer."""
from PIL import Image
import customtkinter as ctk
import os
import subprocess
import sys

from utils.app_select_button import AppSelectButton
from apps.update_settings import SettingsEditor

def get_resource_path(relative_path):
    """Get absolute path to resource, compatible with PyInstaller or development."""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in development mode
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_path, relative_path)

unicorn_image_path = get_resource_path(os.path.join("assets", "Unicorn_logo_nobg2.png"))
print(unicorn_image_path)
print("Exists?", os.path.exists(unicorn_image_path))

original_image = Image.open(unicorn_image_path)
unicorn_image = ctk.CTkImage(light_image=original_image, size=(100, 100))
flipped_unicorn_image = ctk.CTkImage(
    light_image=original_image.transpose(Image.FLIP_LEFT_RIGHT),
    size=(100, 100))


class Header(ctk.CTkFrame):
    """Create header."""

    def __init__(self, parent, height, width, title="My app"):
        """Initialize header."""
        super().__init__(parent, height=height, width=width)
        # create frame
        layout_frame = ctk.CTkFrame(
            self,
            height=height,
            width=width,
            fg_color='transparent')
        layout_frame.pack(fill="both", expand=True)

        # left image
        left_image_label = ctk.CTkLabel(
            layout_frame,
            image=unicorn_image,
            text="")
        left_image_label.pack(side="left", padx=(10, 0))

        # left spacer
        left_spacer = ctk.CTkLabel(layout_frame, text="")
        left_spacer.pack(side="left", expand=True)

        # title
        title_label = ctk.CTkLabel(
            layout_frame,
            text=title,
            font=("Arial", 24))
        title_label.pack(side="left")

        # right spacer
        right_spacer = ctk.CTkLabel(layout_frame, text="")
        right_spacer.pack(side="left", expand=True)

        # right image
        right_image_label = ctk.CTkLabel(
            layout_frame,
            image=flipped_unicorn_image,
            text="")
        right_image_label.pack(side="right", padx=(0, 10))


class Footer(ctk.CTkFrame):
    """Create footer."""

    def __init__(self, parent, height, width, on_settings_updated=None, **kwargs):
        """Initialize footer."""
        super().__init__(parent, height=height, width=width)
        self.on_settings_updated = on_settings_updated
        edit_settings_button = AppSelectButton(
            self,
            text="Edit Settings",
            command=self.open_edit_settings
        )
        edit_settings_button.pack(pady=5)

    def open_edit_settings(self):
        """Open edit settings menu for the application."""
        SettingsEditor(on_save_callback=self.on_settings_updated)





