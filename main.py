import os

import customtkinter as ctk
import subprocess
from configparser import ConfigParser
import os

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme('themes/main_theme.json')

        image_path = os.path.join("assets", "Unicorn_logo_nobg2.png")

        if not os.path.exists(image_path):
            print(f"Error, image file not found: {image_path}")
            exit()

        self.settings = self.load_settings()

        self.title(f"{self.settings['App']['title']}")
        self.geometry(f"{self.settings['MainWindow']['width']}x{self.settings['MainWindow']['height']}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.header_frame = ctk.CTkFrame(self, height=int(int(self.settings['MainWindow']['height']) * .1), width=int(self.settings['MainWindow']['width']))
        self.header_frame.grid(column=0, row=0, padx=10, pady=10, sticky='n')

        self.footer_frame =ctk.CTkFrame(self, height=int(int(self.settings['MainWindow']['height']) * .1), width=int(self.settings['MainWindow']['width']))
        self.footer_frame.grid(column=0, row=2, padx=10, pady=10, sticky='s')

        self.main_frame = ctk.CTkFrame(self, fg_color="blue", corner_radius=0)
        self.main_frame.grid(column=0, row=1, padx= 10, sticky="nsew")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)







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