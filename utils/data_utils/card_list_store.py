"""Singleton for storing the card shop dump."""
from utils.config_utils.settings import settings as settings_module
from utils.data_utils.data_store import DataStore
import pandas as pd


class CardListStore:
    _instance = None
    _card_list_dataframe = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CardListStore, cls).__new__(cls)
        return cls._instance

    def load_card_list(self):
        print("Loading card list")
        file_path = settings_module['InitialFileDirs']['target_card_list_file']
        self._card_list_dataframe = pd.read_csv(file_path)

    def get_card_ratings(self, card_id):
        df1 = self._card_list_dataframe.copy()
        df1 = df1[df1['Card ID'] == int(card_id)]

        return df1


card_store = CardListStore()
