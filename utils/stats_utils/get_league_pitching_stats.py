"""Script for calculating league pitching stats."""
from utils.data_utils.data_store import data_store
from utils.file_utils.process_files import cull_teams
from utils.stats_utils.convert_innings import innings_calc


def get_league_pitching_stats():
    df1 = data_store.get_data().copy()

    df1, removed = cull_teams(df1)

    df1['IPC'] = innings_calc(df1['IP'])
    df1 = df1[['IPC', 'ER', 'K', 'BB.1', 'HR.1']].sum()

    era = ((df1['ER']/df1['IPC'])*9).round(2)
    krate = ((df1['K']/df1['IPC'])*9).round(2)
    bbrate = ((df1['BB.1']/df1['IPC'])*9).round(2)
    hrrate = ((df1['HR.1']/df1['IPC'])*9).round(2)

    league_stats = [era, krate, bbrate, hrrate]
    del df1
    return league_stats