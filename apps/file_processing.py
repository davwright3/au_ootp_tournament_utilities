import tkinter as tk
from pathlib import Path
from tkinter import ttk
from utils.load_settings import load_settings


class FileProcessor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.settings = load_settings()


        self.title("File Processing")
        self.geometry(f"{self.settings['MainWindow']['width']}x{self.settings['MainWindow']['height']}")


if __name__ == '__main__':
    app = FileProcessor()
    app.mainloop()