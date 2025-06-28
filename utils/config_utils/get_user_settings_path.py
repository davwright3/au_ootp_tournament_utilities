"""
Check operating system status.

Utility to check which operating system is
running and adjust user settings path as necessary.
"""

import os
import sys


def get_user_settings_path(app_name):
    """Check OS and routes to user settings path."""
    if os.name == 'nt':
        # Running in Windows
        base_dir = os.getenv('APPDATA', os.path.expanduser('~'))
    elif sys.platform == 'darwin':
        # macos
        base_dir = os.path.expanduser(f'~/Library/Application Support/{app_name}')
    else:
        # Running in linux or other
        base_dir = os.path.expanduser('~/.config/{app_name}')
    return os.path.join(base_dir, app_name, 'settings.ini')
