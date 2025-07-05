"""Utility for getting stats for the league."""
import pandas as pd
from utils.stats_utils.cull_teams import cull_teams

def get_league_batter_stats(df_target=None):
    """Get league stats from a dataframe."""
    df1 = pd.DataFrame(pd.read_csv(df_target))
    df1, removed = cull_teams(df1)

    # df1 to get league stats
    df1 = df1[['CID', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'TB', 'RC', 'SB', 'CS', 'SO', 'ZR', 'BB', 'IBB', 'SF', 'HP']]

    lg_avg = (df1['H'].sum() /df1['AB'].sum()).round(3)
    lg_obp = (
            (df1['H'].sum() + df1['BB'].sum() + df1['HP'].sum()) /
            (df1['AB'].sum() + df1['BB'].sum() + df1['HP'].sum() + df1['SF'].sum()
             )).round(3)
    lg_slg = (df1['TB'].sum()/df1['AB'].sum()).round(3)
    lg_ops = lg_obp + lg_slg
    lg_woba = (((.69*df1['BB'].sum())+ (.72*df1['HP'].sum()) + (.89*df1['1B'].sum()) +
                (1.27*df1['2B'].sum()) + (1.62*df1['3B'].sum()) + (2.10*df1['HR'].sum())) /
               (df1['AB'].sum() + df1['BB'].sum() - df1['IBB'].sum() + df1['SF'].sum() +
                df1['HP'].sum())).round(3)
    lg_hrRate = ((df1['HR'].sum() / df1['PA'].sum())*600).round(2)
    lg_kRate = ((df1['SO'].sum() / df1['PA'].sum())*600).round(2)
    lg_bbRate = ((df1['BB'].sum() / df1['PA'].sum())*600).round(2)

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


