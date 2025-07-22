"""Utility for getting list of teams from dataframe."""
# import pandas as pd


def get_team_list(df):
    """Get unique teams from dataframe."""
    team_list = df['ORG'].unique().tolist()
    team_list.sort()
    return team_list
