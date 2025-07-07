"""Main data storage singleton for stats dataframe."""
import pandas as pd

class DataStore:
    _instance=None
    _main_dataframe=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
        return cls._instance

    def load_data(self, file_path):
        self._main_dataframe = pd.read_csv(file_path)

    def get_data(self):
        return self._main_dataframe

    def set_data(self, new_df):
        self._main_dataframe = new_df

    def clear_data(self):
        self._main_dataframe = None