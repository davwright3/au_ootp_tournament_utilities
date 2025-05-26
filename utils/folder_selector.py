"""Use to open csv file for processing."""
from tkinter import filedialog


def select_folder(parent=None, initial_dir=r"C:\BaseballData\OOTPFiles\Tournaments\RawData"):
    """Open csv file for processing with optional parent window."""
    return filedialog.askdirectory(
        title="Select folder containing raw data",
        parent=parent,
        initialdir=initial_dir
    )

