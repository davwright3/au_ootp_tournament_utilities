"""Use to open csv file for processing."""
from tkinter import filedialog


def open_file():
    """Open csv file for processing."""
    return filedialog.askopenfile(filetypes=[('CSV', '*.csv')])
