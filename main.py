import customtkinter as ctk
import subprocess
from configparser import ConfigParser

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme('themes/main_theme.json')

        self.settings = self.load_settings()

        self.title(f"{self.settings['App']['title']}")
        self.geometry(f"{self.settings['MainWindow']['width']}x{self.settings['MainWindow']['height']}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.header_frame = ctk.CTkFrame(self, height=int(int(self.settings['MainWindow']['height']) * .1), width=int(self.settings['MainWindow']['width']))
        self.header_frame.grid(column=0, row=0, padx=10, pady=10, sticky='n')

        self.footer_frame =ctk.CTkFrame(self, height=int(int(self.settings['MainWindow']['height']) * .1), width=int(self.settings['MainWindow']['width']))
        self.footer_frame.grid(column=0, row=1, padx=10, pady=10, sticky='s')





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