"""Module for returning woba weights."""


def get_woba_weights():
    """Return woba weights."""
    weights = {
        'BB': 0.701,
        'IBB': 0.0,
        'HP': 0.732,
        '1B': 0.895,
        '2B': 1.270,
        '3B': 1.608,
        'HR': 2.072,
        'SF': 0
    }
    return weights


def get_woba_columns():
    """Return woba columns required for calculation."""
    columns = ['AB', 'BB', 'HP', '1B', '2B', '3B', 'HR', 'IBB', 'SF']
    return columns
