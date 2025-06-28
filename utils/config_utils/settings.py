"""Create settings singleton for app use."""
import os
import shutil
import sys
from configparser import ConfigParser
from utils.config_utils.get_user_settings_path import get_user_settings_path

APP_NAME = 'AU Tournament Utilities'


# def get_user_settings_path():
#     """Check OS and find settings path."""
#     if os.name == 'nt':
#         base_dir = os.getenv('APPDATA', os.path.expanduser('~'))
#     else:
#         base_dir = os.path.expanduser('~/config')
#     settings_dir = os.path.join(base_dir, APP_NAME)
#     os.makedirs(settings_dir, exist_ok=True)
#     return os.path.join(settings_dir, 'settings.ini')


def get_default_settings_path():
    """Find the default settings path."""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'settings_default.ini')
    else:
        return os.path.join(
            os.path.dirname(__file__),
            '..',
            'settings_default.ini')


SETTINGS_PATH = get_user_settings_path(APP_NAME)
DEFAULT_SETTINGS_PATH = get_default_settings_path()


def clean_path(path_str, expect_file=False):
    """Clean the path to ensure valid starting directory paths."""
    path_str = path_str.strip().strip('"').strip("'")
    if not path_str:
        return ""
    path_str = os.path.expanduser(path_str)
    path_str = os.path.abspath(path_str)
    if expect_file:
        return path_str if os.path.isfile(path_str) else ""
    return path_str if os.path.isdir(path_str) else ""


def reload_settings():
    """Reload new settings."""
    global settings
    settings = _load()


def ensure_settings_up_to_date():
    """Check that user has most up to date settings."""
    user_config = ConfigParser()
    default_config = ConfigParser()

    default_config.read(DEFAULT_SETTINGS_PATH)

    if not os.path.exists(SETTINGS_PATH):
        try:
            shutil.copyfile(DEFAULT_SETTINGS_PATH, SETTINGS_PATH)
            print("Created user settings from default")
            return
        except Exception as e:
            print(f"Could not copy default settings: {e}")
            return

    user_config.read(SETTINGS_PATH)

    updated = False
    for section in default_config.sections():
        if not user_config.has_section(section):
            user_config.add_section(section)
            print(f"Adding section {section}")
            updated = True
        for key, value in default_config.items(section):
            if not user_config.has_option(section, key):
                user_config.set(section, key, value)
                print(f"Setting {key} to {value}")
                updated = True

    if updated:
        with open(SETTINGS_PATH, 'w') as configfile:
            user_config.write(configfile)
        print("User settings updated with missing defaults")
    else:
        print("User settings already up to date")


def _load():
    """Initialize path and load settings file."""
    ensure_settings_up_to_date()
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
                fallback='AU Tournament Utilities'),
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
            'initial_target_folder': clean_path(config.get(
                'InitialFileDirs',
                'initial_target_folder',
                fallback='')),
            'initial_data_folder': clean_path(config.get(
                'InitialFileDirs',
                'initial_data_folder',
                fallback='')),
            'target_card_list_file': clean_path(config.get(
                'InitialFileDirs',
                'target_card_list_file',
                fallback=''
            ), expect_file=True),
            'target_collection_list_file': clean_path(config.get(
                'InitialFileDirs',
                'target_collection_list_file',
                fallback=''
            ), expect_file=True),
        }

    }


settings = _load()
