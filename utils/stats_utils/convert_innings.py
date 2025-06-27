"""Utility for converting innings into proper format."""


def innings_calc(innings):
    """Convert innings from 1/10's to proper format."""
    whole_innings = round(innings, 0)
    fractional_innings = (innings - whole_innings) / .3
    return whole_innings + fractional_innings
