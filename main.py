import os

import customtkinter as ctk
import subprocess
from configparser import ConfigParser
import os
from utils.app_select_button import AppSelectButton
from PIL import Image, ImageTk

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme('themes/main_theme.json')

        self.settings = self.load_settings()

        self.title(f"{self.settings['App']['title']}")
        self.geometry(f"{self.settings['MainWindow']['width']}x{self.settings['MainWindow']['height']}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header_footer_height = int(int(self.settings["MainWindow"]["height"])*.1)

        unicorn_image_path = os.path.join("assets", "Unicorn_logo_nobg2.png")
        unicorn_image = ctk.CTkImage(light_image=Image.open(unicorn_image_path), size=(100,100))
        image = Image.open(unicorn_image_path)
        flipped_unicorn_image = ctk.CTkImage(image.transpose(Image.FLIP_LEFT_RIGHT), size=(100,100))

        self.header_frame = ctk.CTkFrame(self, height=header_footer_height, width=int(self.settings['MainWindow']['width']))
        self.header_frame.grid(column=0, row=0, padx=10, pady=10, sticky='new')

        self.footer_frame =ctk.CTkFrame(self, height=header_footer_height, width=int(self.settings['MainWindow']['width']))
        self.footer_frame.grid(column=0, row=2, padx=10, pady=10, sticky='sew')

        self.main_frame = ctk.CTkFrame(self, fg_color="blue", corner_radius=0)
        self.main_frame.grid(column=0, row=1, padx= 10, sticky="nsew")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)

        self.header_title = ctk.CTkLabel(self.header_frame, text="Welcome to Angered Unicorn's Tournament Utilities", font=("Arial", 24))
        self.header_title.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

        label = ctk.CTkLabel(self.header_frame, image=unicorn_image, text="")
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        label = ctk.CTkLabel(self.header_frame, image=flipped_unicorn_image, text="")
        label.grid(column=0, row=0, padx=10, pady=10, sticky='e')

        self.file_processing_select_button = AppSelectButton(self.main_frame, text="File Processing")
        self.file_processing_select_button.grid(column=0, row=0, padx=10, pady=10, sticky='ew')







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