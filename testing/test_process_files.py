"""Test methods in process_files utility."""
import os
import sys
import tempfile
import pandas as pd

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.process_files import cull_teams, process_files


def test_cull_teams_removes_high_scoring():
    """Test that cull_teams removes high scoring teams."""
    # Create test data
    data = {
        'ORG': ['A', 'A', 'B', 'B', 'c'],
        'GS.1': [1, 1, 1, 1, 1],
        'R': [10, 10, 5, 4, 3],
    }
    df = pd.DataFrame(data)
    filtered, removed = cull_teams(df)

    assert removed == 1
    assert 'A' not in filtered['ORG'].values


def test_process_files_adds_unique_files():
    """Test that process_files adds unique files."""
    # Create a temporary target csv
    with tempfile.NamedTemporaryFile(
            mode='w+',
            suffix='.csv',
            delete=False) as tmp_target:
        pd.DataFrame(
            columns=[
                'ORG',
                'GS.1',
                'R',
                'Trny']).to_csv(tmp_target.name, index=False)

    # Create temp raw directory with mock files
    with tempfile.TemporaryDirectory() as tmp_raw:
        file1_path = os.path.join(tmp_raw, 'file1.csv')
        pd.DataFrame(
            {'ORG': ['X'],
             'GS.1': [1],
             'R': ['9']}).to_csv(file1_path, index=False)

        result = process_files(tmp_target.name, tmp_raw)

        assert isinstance(result, list)
        assert result[0][0] == "file1"
