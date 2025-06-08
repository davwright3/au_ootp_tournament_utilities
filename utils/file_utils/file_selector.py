"""Use to open csv file for processing."""
from tkinter import filedialog


def open_file(parent=None, initial_dir="/"):
    """Open csv file for processing with optional parent window."""
    return filedialog.askopenfile(
        title="Select target file",
        initialdir=initial_dir,
        filetypes=[('CSV', '*.csv')],
        parent=parent
    )
