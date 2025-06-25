"""Module to calculate basic pitching stats for display in a data frame."""
import pandas as pd
from utils.config_utils import settings as settings_module
from utils.stats_utils.cull_teams import cull_teams


def calc_basic_pitching_stats(
        df_to_load,
        min_ip=100,
        role=None,
        inning_split=4,
        variant_split=False,
        pitching_side=None,
        player_name=None,
        pitching_stats_to_view=None
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

    print("Running basic pitching stat calculation...")

    # Set columns for whether variants will be split or not
    if variant_split:
        columns_to_keep = ['CID', 'Title', 'VLvl', 'Card Value', 'Throws',
                           'IPC']
    else:
        columns_to_keep = ['CID', 'Title', 'Card Value', 'Throws', 'IPC']

    columns_to_keep.extend(pitching_stats_to_view)

    df1, removed = cull_teams(pd.DataFrame(df_to_load))
    print("Removed: ", removed)
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

    df2 = pd.merge(
        card_df[['CID', 'Title', 'Card Value', 'Throws']],
        df2,
        on='CID',
        how='inner'
    )

    lg_era = (df2['ER'].sum()/df2['IPC'].sum())*9
    fip_con = (
            lg_era -
            (((13 * df2['HR.1'].sum()) +
              (3 * (df2['BB.1'].sum() + df2['HP.1'].sum())) -
              (2 * df2['K'].sum()))
             / df2['IPC'].sum()))

    df2['FIP'] = (((13 * df2['HR.1']) +
                   (3 * (df2['BB.1'] + df2['HP.1'])) -
                   (2 * df2['K'])) / df2['IPC']) + fip_con
    df2['ERA'] = (df2['ER']/df2['IPC']) * 9
    df2['K/9'] = (df2['K']/df2['IPC']) * 9
    df2['KPct'] = df2['K']/df2['BF']
    df2['BB/9'] = (df2['BB.1']/df2['IPC']) * 9
    df2['BBPct'] = df2['BB.1']/df2['BF']
    df2['HR/9'] = (df2['HR.1']/df2['IPC']) * 9
    df2['GSPct'] = df2['GS.1']/df2['G.1']
    df2['QSPct'] = df2['QS']/df2['GS.1']
    df2['WHIP'] = (df2['HA'] + df2['BB.1'])/df2['IPC']
    df2['IRSPct'] = df2['IRS']/df2['IR']
    df2['SD/MD'] = df2['SD']/df2['MD']
    df2['IP/G'] = df2['IPC']/df2['G.1']
    df2['WAR/200'] = (df2['WAR.1']/df2['IPC']) * 200

    df3 = df2[df2['IPC'] > min_ip].copy()

    if role == 1:
        df3 = df3[df3["IP/G"] >= inning_split]
    elif role == 2:
        df3 = df3[df3["IP/G"] < inning_split]

    df3['CID'] = df3['CID'].astype(str)
    df3['Title'] = df3['Title'].astype(str)
    df3['Throws'] = df3['Throws'].apply(
        lambda x: 'R' if x == 1 else 'L'
    )
    df3['Card Value'] = df3['Card Value'].astype(str)
    df3['IPC'] = df3['IPC'].apply(lambda x: f"{x:.2f}")
    df3['FIP'] = df3['FIP'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['ERA'] = df3['ERA'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['K/9'] = df3['K/9'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['KPct'] = df3['KPct'].apply(
        lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df3['BB/9'] = df3['BB/9'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['BBPct'] = df3['BBPct'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['HR/9'] = df3['HR/9'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['QSPct'] = df3['QSPct'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['GSPct'] = df3['GSPct'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['WHIP'] = df3['WHIP'].apply(
        lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df3['IRSPct'] = df3['IRSPct'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['SD/MD'] = df3['SD/MD'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['IP/G'] = df3['IP/G'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df3['WAR/200'] = df3['WAR/200'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])

    df3 = df3[columns_to_keep]

    if pitching_side != 'Any':
        df3 = df3[df3['Throws'] == pitching_side]

    if player_name is not None:
        df3 = df3[df3['Title'].str.contains(player_name, case=False, na=False)]

    del df2, df1, removed
    import gc
    gc.collect()

    return df3
