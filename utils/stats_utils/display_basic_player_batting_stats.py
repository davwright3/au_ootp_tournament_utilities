"""Script for calcuating basic batting stats."""
import pandas as pd
# import numpy as np
from utils.config_utils import settings as settings_module
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.calc_basic_batting_stats import calc_basic_batting_stats
from utils.data_utils.data_store import data_store


def display_basic_batting_stats(
        min_pa=1,
        pos=None,
        variant_split=False,
        batter_side=None,
        batter_name=None,
        stats_to_view=None,
        min_value=40,
        max_value=105,):
    """Calculate basic batting stats."""
    df = data_store.get_data()
    df1 = df.copy()
    script_settings = settings_module.settings
    card_df_path = script_settings['InitialFileDirs']['target_card_list_file']
    card_df = pd.DataFrame(pd.read_csv(card_df_path))
    card_df = card_df.rename(
        columns={'Card ID': 'CID', '//Card Title': 'Title'}
    )

    df2, removed = cull_teams(pd.DataFrame(df1))

    columns_from_data = ['CID', 'Title', 'Card Value', 'Bats']

    # Calculate the basic statistics
    if not variant_split:
        columns_to_keep = ['CID', 'Title', 'Bats', 'Card Value',
                           'PA']
        df2 = df2.groupby(
            ['CID'],
            as_index=False)[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR',
                             'IBB', 'BB', 'HP', 'SH', 'SF', 'SO', 'TB',
                             'RC', 'WAR', 'SB', 'CS', 'BsR', 'ZR']].sum()
    else:
        columns_to_keep = ['CID', 'Title', 'VLvl', 'Bats', 'Card Value',
                           'PA']
        df2 = df2.groupby(
            ['CID', 'VLvl'],
            as_index=False)[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR',
                             'IBB', 'BB', 'HP', 'SH', 'SF', 'SO', 'TB',
                             'RC', 'WAR', 'SB', 'CS', 'BsR', 'ZR']].sum()

    columns_to_keep.extend(stats_to_view)

    if pos is None:
        df2 = pd.merge(card_df[columns_from_data], df2, on='CID', how='inner')
    else:
        df2 = pd.merge(card_df[card_df[pos] == 1][columns_from_data],
                       df2,
                       on='CID',
                       how='inner')

    df2 = calc_basic_batting_stats(df2)

    # Create the dataframe to pass to the frame view
    df3 = df2[df2['PA'] > min_pa].copy()
    df3['CID'] = df3['CID'].astype(str)
    df3['Title'] = df3['Title'].astype(str)
    df3['Bats'] = df3['Bats'].apply(
        lambda x: "R" if x == 1 else "L" if x == 2 else "S")
    df3['PA'] = df3['PA'].astype(str)

    df3 = df3[columns_to_keep]
    if batter_side == 'Any':
        df3 = df3
    else:
        df3 = df3[df3['Bats'] == batter_side]

    df3 = df3.rename(columns={"Card Value": 'Val'})
    df3 = df3[(df3['Val'] <= max_value) & (df3['Val'] >= min_value) ]

    if batter_name is not None:
        df3 = df3[df3['Title'].str.contains(batter_name, case=False, na=False)]

    del df, df1, card_df, df2
    import gc
    gc.collect()

    return df3
