"""Retrieve pitcher ratings from card dump."""
import pandas as pd
from utils.data_utils.card_list_store import card_store


def get_pitcher_ratings(card_id):
    pitcher_ratings = card_store.get_card_ratings(card_id=card_id)

    cols = ['//Card Title', 'Stuff', 'Movement', 'Control', 'pHR',
            'pBABIP', 'Stuff vL', 'Movement vL', 'Control vL', 'pHR vL',
            'pBABIP vL', 'Stuff vR', 'Movement vR', 'Control vR', 'pHR vR',
            'pBABIP vR', 'Fastball', 'Slider', 'Curveball', 'Changeup',
            'Cutter', 'Sinker', 'Splitter', 'Forkball', 'Screwball',
            'Circlechange', 'Knucklecurve', 'Knuckleball', 'Stamina', 'Hold']

    return_pitcher_ratings = pitcher_ratings[cols]
    del pitcher_ratings

    return return_pitcher_ratings






