import os
import customtkinter as ctk
from configparser import ConfigParser

class SettingsEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Settings Editor"
        self.geometry = "800x600"

        self.settings_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../settings.ini")
        self.config = ConfigParser()
        self.config.read(self.settings_path)

        self.entries = {}

        row = 0
        for section in self.config.sections():
            ctk.CTkLabel(self, text=f"[{section}]", font=("Arial", 24)).grid(row=row, column=0, columnspan=2, pady=(10, 0), sticky='w' )
            row += 1
            for key, value in self.config.items(section):
                ctk.CTkLabel(self, text=key).grid(row=row, column=0, padx=10, sticky='e')
                entry = ctk.CTkEntry(self)
                entry.insert(0, value)
                entry.grid(row=row, column=1, padx=10, pady=2, sticky='w')
                self.entries[(section, key)] = entry
                row += 1

        save_button = ctk.CTkButton(self, text="Save Settings", command=self.save_settings)
        save_button.grid(row=row, column=0, pady=20)


    def save_settings(self):
        try:
            for(section, key), entry in self.entries.items():
                try:
                    value = entry.get()
                    self.config.set(section, key, value)
                except Exception as e:
                    print(f"Failed to get value for {section}: {key}: {e}")

            with open(self.settings_path, 'w') as configfile:
                self.config.write(configfile)

            print("Settings saved successfully")
            self.destroy()
        except Exception as e:
            print(f"Failed to save settings: {e}")



if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = SettingsEditor()
    app.mainloop()