"""Script for retrieving and passing individual pitcher stats."""
import pandas as pd
from utils.data_utils.data_store import data_store
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.convert_innings import innings_calc


def get_individual_pitcher_stats(cid_value, team=None):
    """Use data store to retrieve individual pitcher stats."""

    columns = ['CID', 'ORG', 'IP', 'G.1', 'GS.1', 'W', 'L', 'SVO', 'SV', 'BS',
               'HLD', 'SD', 'MD', 'BF', 'AB.1', 'HA', '1B.1', '2B.1', '3B.1',
               'HR.1', 'TB.1', 'R.1', 'ER', 'BB.1', 'IBB.1', 'K', 'HP.1', 'SF.1',
               'IR', 'IRS', 'QS', 'GB', 'FB']

    df1 = data_store.get_data().copy()
    df1, deleted = cull_teams(df1)
    df1 = df1[df1['CID'] == int(cid_value)][columns]

    if team is not None:
        df1 = df1[df1['ORG'] == team]

    # If team has no instances of player, df will be empty.
    if df1.empty:
        del df1
        return ['0.00', '0.00', '0.0', '0.0', '0.0']

    df1['IPC'] = innings_calc(df1['IP'])
    df1 = df1[['CID', 'IPC', 'ER', 'BF', 'K', 'BB.1', 'HR.1']].groupby(['CID'], as_index=False).sum()

    innings = df1['IPC'].sum().round(2)
    era = ((df1['ER'].sum()/df1['IPC'].sum())*9).round(2)
    krate = ((df1['K'].sum()/df1['IPC'].sum())*9).round(2)
    bbrate = ((df1['BB.1'].sum()/df1['IPC'].sum())*9).round(2)
    hrrate = ((df1['HR.1'].sum()/df1['IPC'].sum())*9).round(2)



    stats = [innings, era, krate, bbrate, hrrate]
    del df1
    return stats
