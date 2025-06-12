"""Script to check for valid starting path for file selection."""
import os


def confirm_display_path(path, extension):
    """Confirm initial path is valid."""
    if (not path
            or not path.lower().endswith(".csv")
            or not os.path.isfile(path)):
        return (
            f"Please select a valid file with extension {extension}: {path} "
            f"is not valid", False)
    else:
        return path, True
