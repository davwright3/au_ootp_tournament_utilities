"""Instance for storing the overall league stats."""
import pandas as pd
from utils.stats_utils.get_league_batter_stats import get_league_batter_stats

class LeagueStats(object):
    _instance = None
    _league_stats = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LeagueStats, cls).__new__(cls)
        return cls._instance

    def set_league_stats(self):
        self._league_stats = get_league_batter_stats()

    def get_league_stats(self):
        return self._league_stats


league_stats = LeagueStats()