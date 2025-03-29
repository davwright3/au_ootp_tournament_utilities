from configparser import ConfigParser


def load_settings():
    config = ConfigParser()

    try:
        config.read("settings.ini")

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
