"""Utility for getting list of teams from dataframe."""
# import pandas as pd


def get_team_list(df, team_search_name=None):
    """Get unique teams from dataframe."""
    team_list = df['ORG'].dropna().astype(str).unique().tolist()

    if team_search_name is not None:
        team_search_name = team_search_name.lower()
        team_list = [team for team in team_list if team_search_name in team.lower()]
        # print(team_list)

    team_list.sort()
    return team_list
