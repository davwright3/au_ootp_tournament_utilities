"""Module to calculate basic pitching stats for display in a data frame."""
import pandas as pd
from utils.config_utils import settings as settings_module
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.calc_basic_pitching_stats import (
    calc_basic_pitching_stats)
from utils.data_utils.data_store import data_store


def display_basic_pitching_stats(
        min_ip=100,
        role=None,
        inning_split=4,
        variant_split=False,
        pitching_side=None,
        player_name=None,
        pitching_stats_to_view=None,
        min_value=40,
        max_value=105
):
    """Calculate basic pitching stats for display in a data frame."""
    script_settings = settings_module.settings
    card_df_path = script_settings['InitialFileDirs']['target_card_list_file']
    card_df = pd.DataFrame(pd.read_csv(card_df_path))
    card_df = card_df.rename(
        columns={'Card ID': 'CID', '//Card Title': 'Title'}
    )

    def innings_calc(innings):
        whole_innings = round(innings, 0)
        fractional_innings = (innings - whole_innings) / .3
        return whole_innings + fractional_innings

    # Set columns for whether variants will be split or not
    if variant_split:
        columns_to_keep = ['CID', 'Title', 'VLvl', 'Card Value', 'Throws',
                           'IPC']
    else:
        columns_to_keep = ['CID', 'Title', 'Card Value', 'Throws', 'IPC']

    columns_to_keep.extend(pitching_stats_to_view)

    df1, removed = cull_teams(data_store.get_data())
    df1['IPC'] = (df1['IP'].apply(innings_calc))

    if variant_split:
        df2 = df1.groupby(
                by=['CID', 'VLvl'],
                as_index=False)[['IPC', 'G.1', 'GS.1', 'SV',
                                 'SVO', 'BS', 'HLD', 'SD',
                                 'MD', 'BF', 'AB.1', 'HA',
                                 '1B.1', '2B.1', '3B.1', 'HR.1',
                                 'TB.1', 'R.1', 'ER', 'BB.1',
                                 'IBB.1', 'K', 'HP.1', 'SH.1',
                                 'SF.1', 'IR', 'IRS', 'QS', 'CG',
                                 'SHO', 'GB', 'FB', 'WAR.1']].sum()
    else:
        df2 = df1.groupby(
                by=['CID'],
                as_index=False)[['IPC', 'G.1', 'GS.1', 'SV',
                                 'SVO', 'BS', 'HLD', 'SD',
                                 'MD', 'BF', 'AB.1', 'HA',
                                 '1B.1', '2B.1', '3B.1', 'HR.1',
                                 'TB.1', 'R.1', 'ER', 'BB.1',
                                 'IBB.1', 'K', 'HP.1', 'SH.1',
                                 'SF.1', 'IR', 'IRS', 'QS', 'CG',
                                 'SHO', 'GB', 'FB', 'WAR.1']].sum()

    df2 = calc_basic_pitching_stats(df2, min_ip, inning_split, role)

    df3 = pd.merge(
        card_df[['CID', 'Title', 'Card Value', 'Throws']],
        df2,
        on='CID',
        how='inner'
    )

    df3['CID'] = df3['CID'].astype(str)
    df3['Title'] = df3['Title'].astype(str)
    df3['Throws'] = df3['Throws'].apply(
        lambda x: 'R' if x == 1 else 'L'
    )
    df3['Card Value'] = df3['Card Value'].astype(int)
    df3['IPC'] = df3['IPC'].apply(lambda x: f"{float(x):.0f}")
    df3['IP/G'] = df3['IP/G'].apply(lambda x: f"{float(x):.2f}")

    df3 = df3[columns_to_keep]

    if pitching_side != 'Any':
        df3 = df3[df3['Throws'] == pitching_side]

    if player_name is not None:
        df3 = df3[df3['Title'].str.contains(player_name, case=False, na=False)]

    df3 = df3.rename(columns={'Card Value': 'Val'})
    df3 = df3[(df3['Val'] <= max_value) & (df3['Val'] >= min_value)]

    del df2, df1, removed
    import gc
    gc.collect()

    return df3
