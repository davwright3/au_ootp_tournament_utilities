"""Instance for storing the overall league stats in singleton format."""
from utils.stats_utils.get_league_batter_stats import get_league_batter_stats


class LeagueStats(object):
    """Get league batters stats from datafile."""

    _instance = None
    _league_stats = None

    def __new__(cls):
        """Set singleton instance."""
        if cls._instance is None:
            cls._instance = super(LeagueStats, cls).__new__(cls)
        return cls._instance

    def set_league_stats(self):
        """Set the league stats file."""
        self._league_stats = get_league_batter_stats()

    def get_league_stats(self):
        """Return league stats."""
        return self._league_stats


league_stats = LeagueStats()
