import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import tempfile
from utils.config_utils.settings import _load


def write_test_ini(contents: str) -> str:
    """Write a temporary .ini file with the contents and return its path"""
    tmp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.ini')
    tmp_file.write(contents)
    tmp_file.flush()
    tmp_file.close()
    return tmp_file.name

def test_load_valid_settings(tmp_path, monkeypatch):
    ini_file = write_test_ini("""
[MainWindow]
width = 1024
height = 768

[FileProcessor]
title=Test Title

[InitialFileDirs]
target= C:\\Test\\Target
data = C:\\Test\\Data
"""
)

    #patch the loader to point to the test file
    monkeypatch.setattr('utils.config_utils.settings.SETTINGS_PATH', ini_file)

    cfg = _load()

    assert cfg['MainWindow']['width'] == 1024
    assert cfg['MainWindow']['height'] == 768
    print(cfg['FileProcessor']['title'])
    assert cfg['FileProcessor']['title'] == 'Test Title'



def test_load_missing_section(tmp_path, monkeypatch):
    ini_file = write_test_ini("""
[MainWindow]
width = 800
"""
                              )
    monkeypatch.setattr('utils.config_utils.settings.SETTINGS_PATH', ini_file)

    cfg = _load()

    # Missing section should load defaults or fallback
    assert cfg['MainWindow']['width'] == 800
    assert cfg['FileProcessor']['title'] == "File Processor"
    assert cfg['InitialFileDirs']['target'] == ''

