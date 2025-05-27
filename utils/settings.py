"""Create settings singleton for app use."""
import os
import shutil
from configparser import ConfigParser

SETTINGS_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '../settings.ini')

DEFAULT_SETTINGS_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '../settings_default.ini')


def clean_path(path_str):
    """Clean the path to ensure valid starting directory paths."""
    path_str = path_str.strip().strip('"').strip("'")
    if not path_str:
        return ""
    path_str = os.path.expanduser(path_str)
    path_str = os.path.abspath(path_str)
    return path_str if os.path.isdir(path_str) else ""


def _load():
    """Initialize path and load settings file."""
    config = ConfigParser()

    if not os.path.exists(SETTINGS_PATH):
        shutil.copyfile(DEFAULT_SETTINGS_PATH, SETTINGS_PATH)
    print("No settings file found, creating user settings file.")

    try:
        config.read(SETTINGS_PATH)
    except FileNotFoundError:
        print("No settings file, using defaults.ini")
    except Exception as e:
        print(f" an error occurred: {e}")

    # Build clean directory
    return {
        'MainWindow': {
            'width': config.getint('MainWindow', 'width', fallback=800),
            'height': config.getint('MainWindow', 'height', fallback=600),
        },
        'App': {
            'title': config.get(
                'App',
                'title',
                fallback='Auto Tournament Utilities'),
        },
        'FileProcessor': {
            'title': config.get(
                'FileProcessor',
                'title',
                fallback='File Processor'),
            'width': config.getint(
                'FileProcessor',
                'width',
                fallback=1920),
            'height': config.getint(
                'FileProcessor',
                'height',
                fallback=1080),
        },
        'InitialFileDirs': {
            'target': clean_path(config.get(
                'InitialFileDirs',
                'target',
                fallback='')),
            'data': clean_path(config.get(
                'InitialFileDirs',
                'data',
                fallback='')),
        }

    }


settings = _load()
