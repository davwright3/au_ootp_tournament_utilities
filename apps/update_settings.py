"""Run app for updating program settings."""
import os
import sys

import customtkinter as ctk
import tkinter.filedialog as fd
from configparser import ConfigParser
import utils.settings as settings_module
from utils.get_user_settings_path import get_user_settings_path


APP_NAME = "AU Tournament Utilities"

class SettingsEditor(ctk.CTkToplevel):
    """Create class."""

    def __init__(self, on_save_callback=None):
        """Initialize class."""
        super().__init__()
        self.on_save_callback = on_save_callback
        self.title = "Settings Editor"
        self.geometry = "800x600"

        # Get the settings path
        self.settings_path = get_user_settings_path(APP_NAME)
        self.config = ConfigParser()
        self.config.read(self.settings_path)

        self.entries = {}

        row = 0
        for section in self.config.sections():
            ctk.CTkLabel(
                self, text=f"[{section}]", font=("Arial", 24)).grid(
                row=row,
                column=0,
                columnspan=2,
                pady=(10, 0),
                sticky='w')
            row += 1
            for key, value in self.config.items(section):
                ctk.CTkLabel(self, text=key).grid(
                    row=row,
                    column=0,
                    padx=10,
                    sticky='e')
                entry = ctk.CTkEntry(self)
                entry.insert(0, value)
                entry.grid(row=row, column=1, padx=10, pady=2, sticky='w')
                self.entries[(section, key)] = entry

                # If the key is a file or folder
                if "file" in key or "path" in key or "folder" in key:
                    # This
                    def make_browse_callback(e=entry, k=key):
                        def callback():
                            if "folder" in k or "path" in k:
                                selected = fd.askdirectory(title="Select Folder")
                            else:
                                selected = fd.askopenfilename(title="Select File")
                            if selected:
                                e.delete(0, 'end')
                                e.insert(0, selected)
                            self.lift()
                            self.focus_force()
                        return callback

                    browse_button = ctk.CTkButton(self, text="Browse", command=make_browse_callback(entry, key), width=80)
                    browse_button.grid(column=2, row=row, padx=5, sticky='w')

                row += 1

        save_button = ctk.CTkButton(
            self,
            text="Save Settings",
            command=self.save_settings)
        save_button.grid(row=row, column=0, pady=20)

        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        def release_topmost():
            self.attributes("-topmost", False)

        self.after(10, release_topmost)


    def save_settings(self):
        """Write settings to settings.ini file."""
        try:
            for (section, key), entry in self.entries.items():
                try:
                    value = entry.get()
                    self.config.set(section, key, value)
                except Exception as e:
                    print(f"Failed to get value for {section}: {key}: {e}")

            with open(self.settings_path, 'w') as configfile:
                self.config.write(configfile)

            if self.on_save_callback:
                self.on_save_callback()

            print("Settings saved successfully")
        except Exception as e:
            print(f"Failed to save settings: {e}")




# if __name__ == "__main__":
#     ctk.set_appearance_mode("System")
#     ctk.set_default_color_theme("blue")
#
#     root = ctk.CTk()
#     root.withdraw()
#     editor = SettingsEditor()
#     editor.mainloop()
