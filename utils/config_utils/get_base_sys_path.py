"""Get base system path for program."""
import sys
import os

def get_base_sys_path():
    """Find base path depending on environment."""
    if getattr(sys, 'frozen', False):
        # Running from PyInstaller .exe
        base_dir = sys._MEIPASS
    else:
        # Running from source
        base_dir = os.path.dirname(os.path.abspath(__file__))

    return base_dir
