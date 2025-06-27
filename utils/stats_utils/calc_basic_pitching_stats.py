"""Calculate basic pitching stats."""
# import pandas as pd


def calc_basic_pitching_stats(df, min_ip=200, inning_split=5, role=None):
    """Calculate basic batting stats and return a dataframe."""
    df1 = df.copy()

    lg_era = (df1['ER'].sum()/df1['IPC'].sum())*9
    fip_con = (
            lg_era -
            (((13 * df1['HR.1'].sum()) +
              (3 * (df1['BB.1'].sum() + df1['HP.1'].sum())) -
              (2 * df1['K'].sum()))
             / df1['IPC'].sum()))

    df1['FIP'] = (((13 * df1['HR.1']) +
                   (3 * (df1['BB.1'] + df1['HP.1'])) -
                   (2 * df1['K'])) / df1['IPC']) + fip_con
    df1['ERA'] = (df1['ER']/df1['IPC']) * 9
    df1['K/9'] = (df1['K']/df1['IPC']) * 9
    df1['KPct'] = df1['K']/df1['BF']
    df1['BB/9'] = (df1['BB.1']/df1['IPC']) * 9
    df1['BBPct'] = df1['BB.1']/df1['BF']
    df1['HR/9'] = (df1['HR.1']/df1['IPC']) * 9
    df1['GSPct'] = df1['GS.1']/df1['G.1']
    df1['QSPct'] = df1['QS']/df1['GS.1']
    df1['WHIP'] = (df1['HA'] + df1['BB.1'])/df1['IPC']
    df1['IRSPct'] = df1['IRS']/df1['IR']
    df1['SD/MD'] = df1['SD']/df1['MD']
    df1['IP/G'] = df1['IPC']/df1['G.1']
    df1['WAR/200'] = (df1['WAR.1']/df1['IPC']) * 200

    df1 = df1[df1['IPC'] > min_ip].copy()

    if role == 1:
        df1 = df1[df1["IP/G"] >= inning_split]
    elif role == 2:
        df1 = df1[df1["IP/G"] < inning_split]

    df1['IPC'] = df1['IPC'].apply(lambda x: f"{x:.2f}")
    df1['FIP'] = df1['FIP'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['ERA'] = df1['ERA'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['K/9'] = df1['K/9'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['KPct'] = df1['KPct'].apply(
        lambda x: f"{x*100:.2f}")
    df1['BB/9'] = df1['BB/9'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['BBPct'] = df1['BBPct'].apply(
        lambda x: f"{x*100:.2f}")
    df1['HR/9'] = df1['HR/9'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['QSPct'] = df1['QSPct'].apply(
        lambda x: f"{x*100:.2f}")
    df1['GSPct'] = df1['GSPct'].apply(
        lambda x: f"{x*100:.2f}")
    df1['WHIP'] = df1['WHIP'].apply(
        lambda x: f"{x:.3f}" if x > 1 else f"{x:.3f}"[1:])
    df1['IRSPct'] = df1['IRSPct'].apply(
        lambda x: f"{x*100:.2f}")
    df1['SD/MD'] = df1['SD/MD'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['IP/G'] = df1['IP/G'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])
    df1['WAR/200'] = df1['WAR/200'].apply(
        lambda x: f"{x:.2f}" if x > 1 else f"{x:.2f}"[1:])

    del df
    import gc
    gc.collect()
    return df1
