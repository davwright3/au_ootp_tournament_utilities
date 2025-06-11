import pandas as pd
import numpy as np
from utils.config_utils import settings as settings_module

def calc_basic_batting_stats(df, min_pa = 1, pos = None):
    df1 = pd.DataFrame(df)
    script_settings = settings_module.settings
    card_df_path = script_settings['InitialFileDirs']['target_card_list_file']
    card_df = pd.DataFrame(pd.read_csv(card_df_path))
    card_df = card_df.rename(columns={'Card ID': 'CID', '//Card Title': 'Title'})

    df2 = pd.DataFrame(df1)

    # Calculate the basic statistics
    df2 = df2.groupby(['CID'], as_index=False)[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'IBB',
                                                'BB', 'HP', 'SH', 'SF', 'SO', 'TB', 'RC', 'WAR', 'SB',
                                                'CS', 'BsR', 'ZR']].sum()

    if pos is None:
        df2 = pd.merge(card_df[['CID', 'Title']], df2, on='CID', how='inner')
    else:
        df2 = pd.merge(card_df[card_df[pos]==1], df2, on='CID', how='inner')

    df2['AVG'] = (df2['H']/df2['AB']).round(3)
    df2['OBP'] = ((df2['H'] + df2['BB'] + df2['HP'])/(df2['AB'] + df2['BB'] + df2['HP'] + df2['SF'])).round(3)
    df2['SLG'] = (df2['TB']/df2['AB']).round(3)
    df2['OPS'] = (df2['OBP'] + df2['SLG']).round(3)
    df2['wOBA'] = (
            ((.701*df2['BB']) + (.732*df2['HP']) + (.895*df2['1B'])
            + (1.27*df2['2B']) + (1.608*df2['3B']) + (2.072*df2['HR'])) /
            (df2['AB'] + df2['BB'] - df2['IBB'] + df2['SF'] + df2['HP'])
            ).round(3)
    df2['HR/600'] = ((df2['HR']/df2['PA'])*600).round(1)
    df2['K/600'] = ((df2['SO'] / df2['PA']) * 600).round(1)
    df2['BB/600'] = ((df2['BB']/df2['PA'])*600).round(1)
    df2['SB/600'] = ((df2['SB']/df2['PA'])*600).round(1)
    df2['SBPct'] = np.where(
        (df2['SB'] + df2['CS'])== 0,
        0,
        (df2['SB']/(df2['SB'] + df2['CS'])).round(3))
    df2['RC/600'] = ((df2['RC']/df2['PA'])*600).round(1)
    df2['WAR/600'] = ((df2['WAR']/df2['PA'])*600).round(1)
    df2['BsR/600'] = ((df2['BsR']/df2['PA'])*600).round(2)
    df2['ZR/600'] = ((df2['ZR']/df2['PA'])*600).round(2)

    # Create the dataframe to pass to the frame view
    df3 = df2[df2['PA']>min_pa].copy()
    df3['CID'] = df3['CID'].astype(str)
    df3['Title'] = df3['Title'].astype(str)
    df3['PA'] = df2['PA'].astype(str)
    df3['AVG'] = df2['AVG'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df3['OBP'] = df2['OBP'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df3['SLG'] = df2['SLG'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df3['OPS'] = df2['OPS'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df3['wOBA'] = df2['wOBA'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df3['HR/600'] = df2['HR/600'].apply(lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df3['K/600'] = df2['K/600'].apply(lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df3['BB/600'] = df2['BB/600'].apply(lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df3['SB/600'] = df2['SB/600'].apply(lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df3['SBPct'] = df2['SBPct'].apply(lambda x: f"{x:.2f}"[1:] if x < 1 else f"{x:.2f}")
    df3['RC/600'] = df2['RC/600'].apply(lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")
    df3['WAR/600'] = df2['WAR/600'].apply(lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")
    df3['BsR/600'] = df2['BsR/600'].apply(lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")
    df3['ZR/600'] = df2['ZR/600'].apply(lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")

    columns_to_keep = ['CID', 'Title', 'PA', 'AVG', 'OBP', 'SLG', 'OPS',
                       'wOBA', 'HR/600', 'K/600', 'BB/600', 'SB/600', 'SBPct',
                       'RC/600', 'WAR/600', 'BsR/600', 'ZR/600']

    df3 = df3[columns_to_keep]

    return df3