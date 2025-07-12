"""Module to get individual batter's stats."""
from utils.stats_utils.calculate_return_batting_stats import (
    calculate_ops, calculate_avg, calculate_woba, calculate_obp,
    calculate_slg, calculate_k_rate, calculate_bb_rate, calculate_hr_rate
)


def get_individual_batter_stats(cid_value, player_df, team=None):
    """Get stats for individual batter."""
    df1 = player_df.copy()

    df1 = df1[
        ['CID', 'ORG', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'TB',
         'RC', 'SB', 'CS', 'SO', 'ZR', 'BB', 'IBB', 'SF', 'HP']]
    df1 = df1[df1['CID'] == int(cid_value)]

    if team:
        df2 = df1[df1['ORG'] == team]
        if not df2.empty:
            df1 = df2
            del df2
        else:
            del df2, df1
            return None

    df1 = df1.groupby(['CID']).sum()

    avg = calculate_avg(df1['H'], df1['AB'])
    obp = calculate_obp(df1['H'], df1['BB'], df1['HP'], df1['SF'], df1['AB'])
    slg = calculate_slg(df1['TB'], df1['AB'])
    ops = calculate_ops(obp, slg)
    woba = calculate_woba(df1['BB'], df1['HP'], df1['1B'], df1['2B'],
                          df1['3B'], df1['HR'], df1['AB'], df1['IBB'],
                          df1['SF'])
    hr_rate = calculate_hr_rate(df1['HR'], df1['PA'])
    k_rate = calculate_k_rate(df1['SO'], df1['PA'])
    bb_rate = calculate_bb_rate(df1['BB'], df1['PA'])
    plate_app = int(df1.iloc[0]['PA'])

    batter_stats = [avg, obp, slg, ops, woba, hr_rate,
                    k_rate, bb_rate, plate_app]

    del df1
    import gc
    gc.collect()

    return batter_stats
