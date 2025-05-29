import sys
import os
import tempfile
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import file_selector, folder_selector

def test_open_file_returns_path():
    mock_file = MagicMock()
    mock_file.name = 'mock_file.csv'

    with patch('tkinter.filedialog.askopenfile', return_value=mock_file) as mock_dialog:
        result = file_selector.open_file(initial_dir="C:/Test")
        assert result.name == "mock_file.csv"
        mock_dialog.assert_called_once()

def test_open_folder_returns_path():
    with patch('tkinter.filedialog.askdirectory', return_value="C:/Test/Folder") as mock_dir:
        result = folder_selector.select_folder(initial_dir="C:/Test")
        assert result == "C:/Test/Folder"
        mock_dir.assert_called_once()