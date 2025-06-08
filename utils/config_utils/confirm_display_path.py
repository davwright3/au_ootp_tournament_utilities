import os

def confirm_display_path(path, extension):
    if not path or not path.lower().endswith(".csv") or not os.path.isfile(path):
        return f"Please select a valid file with extension {extension}: {path} is not valid", False
    else:
        return path, True
