"""Module to get individual batter's stats."""
import pandas as pd
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.calculate_return_batting_stats import *

def get_individual_batter_stats(cid_value, df_target, team=None):
    df1, removed = cull_teams(pd.DataFrame(pd.read_csv(df_target)))

    df1 = df1[
        ['CID', 'ORG', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'TB', 'RC', 'SB', 'CS', 'SO', 'ZR', 'BB', 'IBB', 'SF', 'HP']]
    df1 = df1[df1['CID']== int(cid_value)]

    if team:
        df2 = df1[df1['ORG']==team]
        if not df2.empty:
            print(df2.head())
            df1 = df2
            del df2


    df1 = df1.groupby(['CID']).sum()

    avg = calculate_avg(df1['H'], df1['AB'])
    obp = calculate_obp(df1['H'], df1['BB'], df1['HP'], df1['SF'], df1['AB'])
    slg = calculate_slg(df1['TB'], df1['AB'])
    ops = calculate_ops(obp, slg)
    woba = calculate_woba(df1['BB'], df1['HP'], df1['1B'], df1['2B'], df1['3B'], df1['HR'], df1['AB'], df1['IBB'], df1['SF'])
    hrRate = calculate_hr_rate(df1['HR'], df1['PA'])
    kRate = calculate_k_rate(df1['SO'], df1['PA'])
    bbRate = calculate_bb_rate(df1['BB'], df1['PA'])
    plate_app = int(df1.iloc[0]['PA'])

    batter_stats = [avg, obp, slg, ops, woba, hrRate, kRate, bbRate, plate_app]

    del df1, removed
    import gc
    gc.collect()

    return batter_stats