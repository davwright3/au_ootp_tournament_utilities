"""Singleton for storing the card shop dump."""
from utils.config_utils.settings import settings as settings_module
import pandas as pd


class CardListStore:
    """Store card info for selected card."""

    _instance = None
    _card_list_dataframe = None

    def __new__(cls):
        """Instantiate singleton reference."""
        if cls._instance is None:
            cls._instance = super(CardListStore, cls).__new__(cls)
        return cls._instance

    def load_card_list(self):
        """Load card list from file."""
        file_path = settings_module['InitialFileDirs']['target_card_list_file']
        self._card_list_dataframe = pd.read_csv(file_path)

    def get_card_ratings(self, card_id):
        """Get ratings from card for specific player id."""
        df1 = self._card_list_dataframe.copy()
        df1 = df1[df1['Card ID'] == int(card_id)]

        return df1

    def get_all_card_ratings(self):
        """Get a dataframe of all card ratings."""
        return self._card_list_dataframe


card_store = CardListStore()
