"""Utility for getting stats for the league."""
import pandas as pd
import time
from utils.stats_utils.cull_teams import cull_teams
from utils.data_utils.data_store import data_store

def get_league_batter_stats():
    """Get league stats from a dataframe."""
    df = data_store.get_data()
    df1 = df.copy()

    df1, removed = cull_teams(df1)
    # df1 to get league stats
    df1 = df1[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'TB', 'RC', 'SB', 'CS', 'SO', 'ZR', 'BB', 'IBB', 'SF', 'HP']].sum()


    lg_avg = (df1['H'] /df1['AB']).round(3)
    lg_obp = (
            (df1['H'] + df1['BB'] + df1['HP']) /
            (df1['AB'] + df1['BB'] + df1['HP'] + df1['SF']
             )).round(3)
    lg_slg = (df1['TB']/df1['AB']).round(3)
    lg_ops = lg_obp + lg_slg
    lg_woba = (((.69*df1['BB'])+ (.72*df1['HP']) + (.89*df1['1B']) +
                (1.27*df1['2B']) + (1.62*df1['3B']) + (2.10*df1['HR'])) /
               (df1['AB'] + df1['BB'] - df1['IBB'] + df1['SF'] +
                df1['HP'])).round(3)
    lg_hrRate = ((df1['HR'] / df1['PA'])*600).round(2)
    lg_kRate = ((df1['SO'] / df1['PA'])*600).round(2)
    lg_bbRate = ((df1['BB'] / df1['PA'])*600).round(2)

    lg_avg_display = (lambda x: f'{x:.3f}'.lstrip('0'))(lg_avg)
    lg_obp_display = (lambda x: f'{x:.3f}'.lstrip('0'))(lg_obp)
    lg_slg_display = (lambda x: f'{x:.3f}'.lstrip('0'))(lg_slg)
    lg_ops_display = (lambda x: f'{x:.3f}'.lstrip('0'))(lg_ops)
    lg_woba_display = (lambda x: f'{x:.3f}'.lstrip('0'))(lg_woba)
    lg_hrrate_display = (lambda x: f'{x:.2f}'.lstrip('0'))(lg_hrRate)
    lg_kRate_display = (lambda x: f'{x:.2f}'.lstrip('0'))(lg_kRate)
    lg_bbRate_display = (lambda x: f'{x:.2f}'.lstrip('0'))(lg_bbRate)

    lg_stats = [lg_avg_display, lg_obp_display, lg_slg_display, lg_ops_display, lg_woba_display, lg_hrrate_display, lg_kRate_display, lg_bbRate_display]

    del df1, removed
    import gc
    gc.collect()

    return lg_stats


