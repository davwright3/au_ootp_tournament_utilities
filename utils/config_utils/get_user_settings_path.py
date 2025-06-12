"""
Check operating system status.

Utility to check which operating system is
running and adjust user settings path as necessary.
"""

import os


def get_user_settings_path(app_name):
    """Check OS and routes to user settings path."""
    if os.name == 'nt':
        # Running in Windows
        base_dir = os.getenv('APPDATA', os.path.expanduser('~'))
    else:
        # Running in non-windows
        base_dir = os.path.expanduser('~/.config')
    return os.path.join(base_dir, app_name, 'settings.ini')
