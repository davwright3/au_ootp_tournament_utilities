"""Utility for getting team stats"""
import pandas as pd
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.convert_innings import innings_calc

def calc_basic_team_stats(df):
    """Calculate basic team stats"""
    columns_to_keep = ['ORG', 'GP', 'W', 'L', 'Win%', 'AVG', 'OBP', 'SLG',
                       'OPS', 'wOBA', 'ERA']

    df1 = df.copy()
    df1 = df1.groupby('ORG', as_index=False)[['W','L']].sum()
    df1['GP'] = df1['W'] + df1['L']
    df1['Win%'] = (df1['W']/(df1['W'] + df1['L'])).round(3)

    df2 = df.copy()
    df3, removed = cull_teams(pd.DataFrame(df2))
    df3['IPC'] = df3['IP'].apply(innings_calc)
    df3 = df3.groupby(
        'ORG',
        as_index=False)[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR',
                         'R', 'BB', 'IBB', 'HP', 'SB', 'CS',
                         'SF', 'SO', 'TB', 'RC', 'WAR', 'IPC', 'BF',
                         'AB.1', 'HA', '1B.1', '2B.1', '3B.1',
                         'HR.1', 'R.1', 'ER', 'BB.1', 'IBB.1',
                         'K', 'HP.1', 'SF.1', 'GS.1', 'QS', 'WAR.1']].sum()

    df3['AVG'] = (df3['H']/df3['AB']).round(3)
    df3['OBP'] = ((df3['H'] + df3['BB'] + df3['HP'])/(df3['AB'] + df3['BB'] + df3['HP'] + df3['SF'])).round(3)
    df3['SLG'] = (df3['TB']/df3['AB']).round(3)
    df3['OPS'] = df3['OBP'] + df3['SLG']
    df3['wOBA'] = (((.701*df3['BB']) + (.732*df3['HP']) + (.895*df3['1B']) +
                    (1.27*df3['2B']) + (1.608*df3['3B']) + (2.072*df3['HR'])) /
                   (df3['AB'] + df3['BB'] - df3['IBB'] + df3['SF'] + df3['HP'])
                   ).round(3)
    df3['ERA'] = ((df3['ER']/df3['IPC'])*9).round(2)


    df4 = pd.merge(df1, df3, on='ORG', how='left')

    df4['Win%'] = df4["Win%"].apply(lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df4['AVG'] = df4['AVG'].apply(lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df4['OBP'] = df4['OBP'].apply(lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df4['SLG'] = df4['SLG'].apply(lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df4['OPS'] = df4['OPS'].apply(lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df4['wOBA'] = df4['wOBA'].apply(lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df4['ERA'] = df4['ERA'].apply(lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])





    df4 = df4[columns_to_keep]
    del df, df1, df2, df3
    import gc
    gc.collect()
    return df4
