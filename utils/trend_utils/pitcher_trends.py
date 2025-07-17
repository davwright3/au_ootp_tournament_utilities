"""Script for getting a dataframe with pitcher trends over time."""
from utils.stats_utils.convert_innings import innings_calc


def get_pitcher_trends(df, window=5, stat_options=None):
    """Return a dataframe with pitcher trends over time."""
    df['IPC'] = innings_calc(df['IP'])

    list_of_dataframes = []

    if stat_options['innings']:
        innings = get_rolling_innings(df, window)
        list_of_dataframes.append(innings)

    if stat_options['era']:
        era = get_rolling_era(df, window)
        list_of_dataframes.append(era)

    if stat_options['bb']:
        walks = get_rolling_walk_rate(df, window)
        list_of_dataframes.append(walks)

    if stat_options['k9']:
        strikeouts = get_rolling_strikeout_rate(df, window)
        list_of_dataframes.append(strikeouts)

    if stat_options['hr']:
        homeruns = get_rolling_homerun_rate(df, window)
        list_of_dataframes.append(homeruns)

    return list_of_dataframes


def get_rolling_innings(df, window):
    """Return a dataframe with rolling innings over time."""
    innings_df = df.copy()
    innings_df = innings_df.groupby(['Trny'], as_index=False).sum()
    innings_df['rolling_innings'] = innings_df['IPC'].rolling(window).sum()
    max_rolling = innings_df['rolling_innings'].max()
    innings_df['rolling_innings'] = (
            (innings_df['rolling_innings'] / max_rolling) * 7
    )

    innings_df = innings_df[['Trny', 'rolling_innings']]
    return innings_df


def get_rolling_era(df, window):
    """Return a dataframe with rolling era over time."""
    era_df = df.copy()
    era_df = era_df.groupby(['Trny'], as_index=False).sum()
    era_df['rolling_innings'] = era_df['IPC'].rolling(window).sum()
    era_df['rolling_eearned_runs'] = era_df['ER'].rolling(window).sum()
    era_df['rolling_era'] = (
        ((era_df['rolling_eearned_runs'] / era_df['rolling_innings'])*9)
        .round(2)
    )

    era_df = era_df[['Trny', 'rolling_era']]
    return era_df


def get_rolling_walk_rate(df, window):
    """Return a dataframe with rolling walk rate over time."""
    walks_df = df.copy()
    walks_df = walks_df.groupby(['Trny'], as_index=False).sum()
    walks_df['rolling_innings'] = walks_df['IPC'].rolling(window).sum()
    walks_df['rolling_walks'] = walks_df['BB.1'].rolling(window).sum()
    walks_df['walk_rate'] = (
        ((walks_df['rolling_walks'] / walks_df['rolling_innings'])*9)
        .round(2)
    )
    walks_df = walks_df[['Trny', 'walk_rate']]
    return walks_df


def get_rolling_strikeout_rate(df, window):
    """Return a dataframe with rolling strikeout rate over time."""
    strikeout_df = df.copy()
    strikeout_df = strikeout_df.groupby(['Trny'], as_index=False).sum()
    strikeout_df['rolling_innings'] = strikeout_df['IPC'].rolling(window).sum()
    strikeout_df['rolling_strikeout'] = strikeout_df['K'].rolling(window).sum()
    strikeout_df['rolling_strikeout_rate'] = (
        ((strikeout_df['rolling_strikeout'] /
          strikeout_df['rolling_innings'])*9)
        .round(2)
    )
    strikeout_df = strikeout_df[['Trny', 'rolling_strikeout_rate']]
    return strikeout_df


def get_rolling_homerun_rate(df, window):
    """Return a dataframe with rolling homerun rate over time."""
    homerun_df = df.copy()
    homerun_df = homerun_df.groupby(['Trny'], as_index=False).sum()
    homerun_df['rolling_innings'] = homerun_df['IPC'].rolling(window).sum()
    homerun_df['rolling_homeruns'] = homerun_df['HR.1'].rolling(window).sum()
    homerun_df['rolling_homerun_rate'] = (
        ((homerun_df['rolling_homeruns'] / homerun_df['rolling_innings'])*9)
        .round(2)
    )
    homerun_df = homerun_df[['Trny', 'rolling_homerun_rate']]
    return homerun_df
