"""Script for getting a dataframe with pitcher trends over time."""
import pandas as pd
from utils.stats_utils.convert_innings import innings_calc


def get_pitcher_trends(df):
    """Return a dataframe with pitcher trends over time."""
    df['IPC'] = innings_calc(df['IP'])


    df1 = df.copy()
    df1 = df1.groupby(['Trny'], as_index=False).sum()
    df1['rolling_innings'] = df1['IPC'].rolling(5).mean()
    df1 = df1[['Trny', 'IPC']]
    return df1