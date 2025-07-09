"""Main data storage singleton for stats dataframe."""
import pandas as pd
import numpy as np
import datetime

class DataStore:
    _instance=None
    _main_dataframe=None
    trny_format=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
        return cls._instance

    def load_data(self, file_path):
        df = pd.read_csv(file_path)
        df = self.process_trny_column(df)
        self._main_dataframe = df

    def process_trny_column(self, df, column_name='Trny'):
        """Detect trny format and convert to datetime as applicable."""
        try:
            sample = df[column_name].dropna().iloc[0]

            # Try DD MMM format
            try:
                current_year = datetime.datetime.now().year
                parsed_dates = pd.to_datetime(df[column_name], format='%d %b', errors='coerce')
                parsed_dates = parsed_dates.apply(lambda d: d.replace(year=current_year) if pd.notnull(d) else d)
                df[column_name] = parsed_dates
                self.trny_format = 'date_format'
                return df
            except Exception:
                pass

            # Check if it is int format
            if isinstance(sample, np.integer):
                self.trny_format = 'int_format'
                print(df[column_name].head())
                return df

            # Fallback for unknown type
            self.trny_format = 'unknown_format'
            print(df[column_name].head())
            return df

        except (KeyError, IndexError):
            self.trny_format = 'unknown_format'
            return df


    def get_data(self):
        return self._main_dataframe

    def set_data(self, new_df):
        self._main_dataframe = new_df

    def clear_data(self):
        self._main_dataframe = None

data_store = DataStore()