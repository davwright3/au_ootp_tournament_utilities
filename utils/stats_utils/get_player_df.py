"""Module for getting a single dataframe for an individual player."""


from utils.stats_utils.cull_teams import cull_teams
from utils.data_utils.data_store import data_store


def get_player_df(df_filepath, card_id):
    """Get dataframe with individual player stats."""
    df = data_store.get_data()
    df1 = df.copy()
    df1, removed = cull_teams(df1)
    df2 = df1[df1['CID'] == int(card_id)]
    del df1, removed
    import gc
    gc.collect()
    return df2
