from tkinter import filedialog


def open_file():
    return filedialog.askopenfile(filetypes=[('CSV', '*.csv')])
