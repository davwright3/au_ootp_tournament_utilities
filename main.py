import customtkinter as ctk
import subprocess
from configparser import ConfigParser

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.settings = self.load_settings()

        self.title(f"{self.settings['App']['title']}")
        self.geometry(f"{self.settings['Window']['width']}x{self.settings['Window']['height']}")


    def load_settings(self):
        config = ConfigParser()

        try:
            config.read("settings.ini")

            for section in config.sections():
                print(f"[{section}]")
                for key, value in config.items(section):
                    print(f"{key} = {value}")
                print()

        except FileNotFoundError:
            print("Error opening settings.ini")
        except Exception as e:
            print(f" an error occurred: {e}")

        return config


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()