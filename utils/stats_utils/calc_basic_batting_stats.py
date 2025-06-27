"""Calculate basic batting stats."""

# import pandas as pd
import numpy as np


def calc_basic_batting_stats(df):
    """Calculate basic batting stats and return a dataframe."""
    df1 = df.copy()
    df1['AVG'] = (df1['H']/df1['AB']).round(3)
    df1['OBP'] = ((df1['H'] + df1['BB'] +
                   df1['HP'])/(df1['AB'] + df1['BB'] +
                               df1['HP'] + df1['SF'])).round(3)
    df1['SLG'] = (df1['TB']/df1['AB']).round(3)
    df1['OPS'] = df1['OBP'] + df1['SLG']
    df1['wOBA'] = (((.701*df1['BB']) + (.732*df1['HP']) + (.895*df1['1B']) +
                    (1.27*df1['2B']) + (1.608*df1['3B']) + (2.072*df1['HR'])) /
                   (df1['AB'] + df1['BB'] - df1['IBB'] + df1['SF'] + df1['HP'])
                   ).round(3)
    df1['HR/600'] = ((df1['HR']/df1['PA'])*600).round(1)
    df1['K/600'] = ((df1['SO'] / df1['PA']) * 600).round(1)
    df1['BB/600'] = ((df1['BB']/df1['PA'])*600).round(1)
    df1['SB/600'] = ((df1['SB']/df1['PA'])*600).round(1)
    df1['SBPct'] = np.where(
        (df1['SB'] + df1['CS']) == 0,
        0,
        (df1['SB']/(df1['SB'] + df1['CS'])).round(3))
    df1['RC/600'] = ((df1['RC']/df1['PA'])*600).round(1)
    df1['WAR/600'] = ((df1['WAR']/df1['PA'])*600).round(1)
    df1['BsR/600'] = ((df1['BsR']/df1['PA'])*600).round(2)
    df1['ZR/600'] = ((df1['ZR']/df1['PA'])*600).round(2)

    df1['AVG'] = df1['AVG'].apply(
        lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df1['OBP'] = df1['OBP'].apply(
        lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df1['SLG'] = df1['SLG'].apply(
        lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df1['OPS'] = df1['OPS'].apply(
        lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df1['wOBA'] = df1['wOBA'].apply(
        lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df1['HR/600'] = df1['HR/600'].apply(
        lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df1['K/600'] = df1['K/600'].apply(
        lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df1['BB/600'] = df1['BB/600'].apply(
        lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df1['SB/600'] = df1['SB/600'].apply(
        lambda x: f"{x:.1f}"[1:] if x < 1 else f"{x:.1f}")
    df1['SBPct'] = df1['SBPct'].apply(
        lambda x: f"{x:.2f}"[1:] if x < 1 else f"{x:.2f}")
    df1['RC/600'] = df1['RC/600'].apply(
        lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")
    df1['WAR/600'] = df1['WAR/600'].apply(
        lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")
    df1['BsR/600'] = df1['BsR/600'].apply(
        lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")
    df1['ZR/600'] = df1['ZR/600'].apply(
        lambda x: f"{x:.1f}"[1:] if -1 < x < 1 else f"{x:.1f}")

    del df
    import gc
    gc.collect()
    return df1
