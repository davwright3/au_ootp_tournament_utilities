"""Utility for getting team stats."""
import pandas as pd
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.convert_innings import innings_calc
from utils.stats_utils.calc_basic_batting_stats import calc_basic_batting_stats
from utils.stats_utils.calc_basic_pitching_stats import (
    calc_basic_pitching_stats)


def display_basic_team_stats(df,
                             batting_stats_to_display=None,
                             pitching_stats_to_display=None):
    """Calculate basic team stats."""
    columns_to_keep = ['ORG', 'GP', 'W', 'L', 'Win%']
    if batting_stats_to_display is not None:
        columns_to_keep.extend(batting_stats_to_display)
    if pitching_stats_to_display is not None:
        columns_to_keep.extend(pitching_stats_to_display)

    df1 = df.copy()
    df1 = df1.groupby('ORG', as_index=False)[['W', 'L']].sum()
    df1['GP'] = df1['W'] + df1['L']
    df1['Win%'] = (df1['W']/(df1['W'] + df1['L'])).round(3)

    df2 = df.copy()
    df3, removed = cull_teams(pd.DataFrame(df2))
    df3['IPC'] = df3['IP'].apply(innings_calc)
    df3 = df3.groupby(
        'ORG',
        as_index=False)[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR',
                         'R', 'BB', 'IBB', 'HP', 'SB', 'CS',
                         'SF', 'SO', 'TB', 'RC', 'BsR', 'ZR',
                         'WAR', 'IPC', 'G.1', 'BF', 'AB.1', 'HA',
                         '1B.1', '2B.1', '3B.1', 'HR.1', 'R.1',
                         'ER', 'IR', 'IRS', 'SD', 'MD', 'BB.1',
                         'IBB.1', 'K', 'HP.1', 'SF.1', 'GS.1',
                         'QS', 'WAR.1']].sum()

    df3 = calc_basic_batting_stats(df3)
    df3 = calc_basic_pitching_stats(df3)


    df4 = pd.merge(df1, df3, on='ORG', how='left')

    df4 = df4[columns_to_keep]
    del df, df1, df2, df3
    import gc
    gc.collect()
    return df4
