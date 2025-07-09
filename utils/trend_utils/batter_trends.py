"""Utility for getting a player's plate appearance trend."""
from utils.data_utils.get_woba_info import get_woba_weights, get_woba_columns

def get_plate_appearance_trend(df):
    """Return a dataframe for displaying PA trend in matplotlib figure."""
    window = 5
    df1 = df.copy()

    df1 = df1[['Trny', 'PA']].groupby(['Trny'], as_index=False).sum()

    # Rolling plate appearances
    plate_app_df = df1.copy()
    plate_app_df['PA_roll'] = plate_app_df['PA'].rolling(window=window, min_periods=1).sum().astype(int)
    plate_app_df = plate_app_df.drop(columns=['PA'])
    max_pa = plate_app_df['PA_roll'].max()
    min_pa = plate_app_df['PA_roll'].min()
    plate_app_df['PA_roll'] = plate_app_df['PA_roll']/(max_pa - min_pa)  # normalize the plate appearance
    plate_app_df['PA_roll'] = plate_app_df['PA_roll'] * .3 + .1
    plate_app_df.loc[: window-2, 'PA_roll'] = None

    # Calculate rolling woba

    weights = get_woba_weights()
    columns = ['Trny', 'AB', 'BB', 'HP', '1B', '2B', '3B', 'HR', 'IBB', 'SF']
    woba_df = df[columns].copy()
    woba_df = woba_df.groupby(['Trny'], as_index=False).sum()

    woba_df['BB_rolling'] = woba_df['BB'].rolling(window=window, min_periods=1).sum()
    woba_df['HP_rolling'] = woba_df['HP'].rolling(window=window, min_periods=1).sum()
    woba_df['1B_rolling'] = woba_df['1B'].rolling(window=window, min_periods=1).sum()
    woba_df['2B_rolling'] = woba_df['2B'].rolling(window=window, min_periods=1).sum()
    woba_df['3B_rolling'] = woba_df['3B'].rolling(window=window, min_periods=1).sum()
    woba_df['HR_rolling'] = woba_df['HR'].rolling(window=window, min_periods=1).sum()
    woba_df['AB_rolling'] = woba_df['AB'].rolling(window=window, min_periods=1).sum()
    woba_df['IBB_rolling'] = woba_df['IBB'].rolling(window=window, min_periods=1).sum()
    woba_df['SF_rolling'] = woba_df['SF'].rolling(window=window, min_periods=1).sum()
    woba_df['HP_rolling'] = woba_df['HP'].rolling(window=window, min_periods=1).sum()

    woba_df['woba_numerator'] = (
        weights['BB'] * woba_df['BB_rolling'] +
        weights['HP'] * woba_df['HP_rolling'] +
        weights['1B'] * woba_df['1B_rolling'] +
        weights['2B'] * woba_df['2B_rolling'] +
        weights['3B'] * woba_df['3B_rolling'] +
        weights['HR'] * woba_df['HR_rolling']
    )

    woba_df['woba_denominator'] = (
        woba_df['AB_rolling'] + woba_df['BB_rolling'] -woba_df['IBB_rolling'] + woba_df['SF_rolling'] + woba_df['HP_rolling']
    )

    woba_df['wOBA_rolling'] = woba_df['woba_numerator'] / woba_df['woba_denominator']
    woba_df = woba_df[['Trny', 'wOBA_rolling']]


    del df1
    return woba_df, plate_app_df
