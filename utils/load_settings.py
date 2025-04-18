import os
from configparser import ConfigParser


def load_settings():
    ini_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../settings.ini')

    config = ConfigParser()

    try:
        config.read(ini_path)

        for section in config.sections():
            print(f"[{section}]")
            for key, value in config.items(section):
                print(f"{key} = {value}")
            print()

    except FileNotFoundError:
        print("Error opening settings.ini")
    except Exception as e:
        print(f" an error occurred: {e}")

    return config
