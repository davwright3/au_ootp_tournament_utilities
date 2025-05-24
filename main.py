import customtkinter as ctk
import subprocess
import os
from utils.app_select_button import AppSelectButton
from PIL import Image, ImageTk
from utils.load_settings import load_settings



class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme('themes/main_theme.json')


        #load settings from load_settings utility
        self.settings = load_settings()
        self.title(f"{self.settings['App']['title']}")
        self.geometry(f"{self.settings['MainWindow']['width']}x{self.settings['MainWindow']['height']}")

        """variables for page sizing"""
        header_footer_height = int(int(self.settings["MainWindow"]["height"])*.1)


        """Set grids for the main page"""
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        unicorn_image_path = os.path.join("assets", "Unicorn_logo_nobg2.png")
        unicorn_image = ctk.CTkImage(light_image=Image.open(unicorn_image_path), size=(100,100))
        image = Image.open(unicorn_image_path)
        flipped_unicorn_image = ctk.CTkImage(image.transpose(Image.FLIP_LEFT_RIGHT), size=(100,100))


        """Create header frame"""
        self.header_frame = ctk.CTkFrame(self, height=header_footer_height, width=int(self.settings['MainWindow']['width']))
        self.header_frame.grid(column=0, row=0, padx=10, pady=10, sticky='new')

        self.header_frame.grid_columnconfigure(0, weight=1)


        """Create main frame"""
        self.main_frame = ctk.CTkFrame(self, corner_radius=5)
        self.main_frame.grid(column=0, row=1, padx=10, sticky="nsew")

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)


        """Create footer frame"""
        self.footer_frame =ctk.CTkFrame(self, height=header_footer_height, width=int(self.settings['MainWindow']['width']))
        self.footer_frame.grid(column=0, row=2, padx=10, pady=10, sticky='sew')

        """Header frame data"""
        self.header_title = ctk.CTkLabel(self.header_frame, text="Welcome to Angered Unicorn's Tournament Utilities", font=("Arial", 24))
        self.header_title.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

        label = ctk.CTkLabel(self.header_frame, image=unicorn_image, text="")
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        label = ctk.CTkLabel(self.header_frame, image=flipped_unicorn_image, text="")
        label.grid(column=0, row=0, padx=10, pady=10, sticky='e')


        """Main frame data"""
        self.file_processing_select_button = AppSelectButton(self.main_frame, command=open_file_processing, text="File Processing")
        self.file_processing_select_button.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')


"""This method will open the file processing app in a new window"""
def open_file_processing():
    subprocess.Popen(["python", "apps/file_processing.py"])



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()