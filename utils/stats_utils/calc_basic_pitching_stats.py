"""Module to calculate basic pitching stats for display in a data frame"""
import pandas as pd
from utils.config_utils import settings as settings_module
import numpy as np


def calc_basic_pitching_stats(df_to_load, min_ip = 1, role = None):
    """Calculate basic pitching stats for display in a data frame"""

    def innings_calc(innings):
        whole_innings = round(innings, 0)
        fractional_innings = (innings - whole_innings) / .3
        return whole_innings + fractional_innings

    print("Running basic pitching stat calculation...")

    df1 = pd.DataFrame(df_to_load)
    df1['IPC'] = (df1['IP'].apply(innings_calc)).round(2)
    df2 = df1.groupby(by=['CID'], as_index=False)[['CID', 'IPC', 'G.1', 'GS.1', 'SV', 'SVO', 'BS', 'HLD',
               'SD', 'MD', 'BF', 'AB.1', 'HA', '1B.1', '2B.1', '3B.1',
               'HR.1', 'TB.1', 'R.1', 'ER', 'BB.1', 'IBB.1', 'K',
               'HP.1', 'SH.1', 'SF.1', 'IR', 'IRS', 'QS', 'CG', 'SHO',
               'GB', 'FB', 'WAR.1']].sum()

    lg_era = (df2['ER'].sum()/df2['IPC'].sum())*9
    print("LG ERA:", lg_era)
    fip_con = (lg_era - (((13 * df2['HR.1'].sum()) + (3 * (df2['BB.1'].sum() + df2['HP.1'].sum())) - (2 * df2['K'].sum())) / df2['IPC'].sum()))
    print("FIP con:", fip_con)
    return df2


