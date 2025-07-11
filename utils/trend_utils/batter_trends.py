"""Utility for getting a player's plate appearance trend."""
from utils.data_utils.get_woba_info import get_woba_weights

def get_player_trends(df, selected_stats=None, window=5):
    """Return a dataframe for displaying PA trend in matplotlib figure."""
    window = 5
    dataframes = []
    df1 = df.copy()

    get_rolling_pa(df1, dataframes)
    get_rolling_woba(df1, dataframes)
    get_rolling_avg(df1, dataframes)
    get_rolling_slg(df1, dataframes)
    get_rolling_obp(df1, dataframes)

    del df1
    return dataframes


def get_rolling_pa(df, df_list=None, window=5):
    """Return a dataframe for displaying PA trend in matplotlib figure."""
    df1 = df.copy()
    df1 = df1[['Trny', 'PA']].groupby(['Trny'], as_index=False).sum()

    # Rolling plate appearances
    plate_app_df = df1.copy()
    plate_app_df['PA_roll'] = plate_app_df['PA'].rolling(window=window, min_periods=1).mean().astype(int)
    plate_app_df = plate_app_df.drop(columns=['PA'])
    max_pa = plate_app_df['PA_roll'].max()
    min_pa = plate_app_df['PA_roll'].min()
    plate_app_df['PA_roll'] = plate_app_df['PA_roll']/max_pa  # normalize the plate appearance
    plate_app_df['PA_roll'] = plate_app_df['PA_roll'] * .3 + .1
    plate_app_df.loc[: window-2, 'PA_roll'] = None

    df_list.append(plate_app_df)
    del plate_app_df

def get_rolling_woba(df, df_list=None, window=5):
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
            woba_df['AB_rolling'] + woba_df['BB_rolling'] - woba_df['IBB_rolling'] + woba_df['SF_rolling'] + woba_df[
        'HP_rolling']
    )

    woba_df['wOBA_rolling'] = woba_df['woba_numerator'] / woba_df['woba_denominator']
    woba_df = woba_df[['Trny', 'wOBA_rolling']]
    df_list.append(woba_df)
    del woba_df

def get_rolling_avg(df, df_list=None, window=5):
    avg_columns = ['Trny', 'AB', 'H']
    avg_df = df[avg_columns].copy()
    avg_df = avg_df.groupby(['Trny'], as_index=False).sum()
    avg_df['ab_rolling'] = avg_df['AB'].rolling(window=window, min_periods=1).sum()
    avg_df['hits_rolling'] = avg_df['H'].rolling(window=window, min_periods=1).sum()
    avg_df['avg_rolling'] = (avg_df['hits_rolling'] / avg_df['ab_rolling']).round(3)
    avg_df = avg_df[['Trny', 'avg_rolling']]
    df_list.append(avg_df)
    del avg_df

def get_rolling_slg(df, df_list=None, window=5):
    # calculate rolling slugging percentage
    slg_columns = ['Trny', 'TB', 'AB']
    slg_df = df[slg_columns].copy()
    slg_df = slg_df.groupby(['Trny'], as_index=False).sum()
    slg_df['ab_rolling'] = slg_df['AB'].rolling(window=window, min_periods=1).sum()
    slg_df['tb_rolling'] = slg_df['TB'].rolling(window=window, min_periods=1).sum()
    slg_df['slg_rolling'] = (slg_df['tb_rolling'] / slg_df['ab_rolling']).round(3)
    slg_df = slg_df[['Trny', 'slg_rolling']]
    df_list.append(slg_df)
    del slg_df

def get_rolling_obp(df, df_list=None, window=5):
    obp_columns = ['Trny', 'AB', 'H', 'BB', 'HP', 'SF']
    obp_df = df[obp_columns].copy()
    obp_df = obp_df.groupby(['Trny'], as_index=False).sum()
    obp_df['rolling_ab'] = obp_df['AB'].rolling(window=window, min_periods=1).sum()
    obp_df['rolling_hits'] = obp_df['H'].rolling(window=window, min_periods=1).sum()
    obp_df['rolling_bb'] = obp_df['BB'].rolling(window=window, min_periods=1).sum()
    obp_df['rolling_hp'] = obp_df['HP'].rolling(window=window, min_periods=1).sum()
    obp_df['rolling_sf'] = obp_df['SF'].rolling(window=window, min_periods=1).sum()
    obp_df['rolling_obp'] = ((obp_df['rolling_hits'] + obp_df['rolling_bb'] +
                              obp_df['rolling_hp']) / (obp_df['rolling_ab'] + obp_df['rolling_hp'] +
                                                       obp_df['rolling_bb'] + obp_df['rolling_sf'])).round(3)
    obp_df = obp_df[['Trny', 'rolling_obp']]
    df_list.append(obp_df)
    del obp_df


