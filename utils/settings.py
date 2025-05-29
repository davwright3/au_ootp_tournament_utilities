"""Create settings singleton for app use."""
import os
import shutil
import sys
from configparser import ConfigParser

APP_NAME = 'AU Tournament Utilities'


def get_user_settings_path():
    if os.name == 'nt':
        base_dir = os.getenv('APPDATA', os.path.expanduser('~'))
    else:
        base_dir = os.path.expanduser('~/config')
    settings_dir = os.path.join(base_dir, APP_NAME)
    os.makedirs(settings_dir, exist_ok=True)
    return os.path.join(settings_dir, 'settings.ini')

def get_default_settings_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'settings_default.ini')
    else:
        return os.path.join(os.path.dirname(__file__), '..', 'settings_default.ini')

SETTINGS_PATH = get_user_settings_path()
DEFAULT_SETTINGS_PATH = get_default_settings_path()


def clean_path(path_str):
    """Clean the path to ensure valid starting directory paths."""
    path_str = path_str.strip().strip('"').strip("'")
    if not path_str:
        return ""
    path_str = os.path.expanduser(path_str)
    path_str = os.path.abspath(path_str)
    return path_str if os.path.isdir(path_str) else ""

def reload_settings():
    global settings
    settings = _load()


def _load():
    """Initialize path and load settings file."""
    config = ConfigParser()

    if not os.path.exists(SETTINGS_PATH):
        try:
            shutil.copyfile(DEFAULT_SETTINGS_PATH, SETTINGS_PATH)
            print("No settings file found, creating user settings file...")
        except Exception as e:
            print(f"Could not copy default settings: {e}")

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
