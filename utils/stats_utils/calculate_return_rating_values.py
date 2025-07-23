"""Calculate rating values using user weights."""
import pandas as pd


def calculate_return_rating_values(
        df,
        ratings_to_view=None,
        min_rating=40,
        max_rating=105,
        batting_weights=None,
        pitching_weights=None,
        defense_weights=None
):
    """Calculate ratings and return a dataframe with requested ratings."""
    columns_to_keep = ['CID', 'Title', 'Val']
    columns_to_keep.extend(ratings_to_view)

    df1 = df.copy()
    df1 = df1[['Card ID', "//Card Title", 'Card Value', 'Card Type', 'Year', 'Bats', 'Throws',
               'Contact', 'Gap', 'Power', 'Eye', 'Avoid Ks', 'BABIP', 'Contact vL', 'Gap vL', 'Power vL',
               'Eye vL', 'Avoid K vL', 'BABIP vL', 'Contact vR', 'Gap vR', 'Power vR', 'Eye vR',
               'Avoid K vR', 'BABIP vR', 'Speed', 'Steal Rate', 'Stealing', 'Baserunning',
               'CatcherAbil', 'CatcherFrame', 'Catcher Arm', 'Infield Range', 'Infield Error',
               'Infield Arm', 'DP', 'OF Range', 'OF Error', 'OF Arm', 'Stuff', 'pHR', 'pBABIP',
               'Control', 'Stuff vL', 'pHR vL', 'pBABIP vL', 'Control vL', 'Stuff vR', 'pHR vR',
               'pBABIP vR', 'Control vR']]
    df1 = df1.rename(columns={'Card ID': 'CID', "//Card Title": "Title", 'Card Value': 'Val'})
    df1 = df1[(df1['Val'] >= int(min_rating)) & (df1['Val'] <= int(max_rating))]

    calculate_batting_overall_rating(df1, batting_weights)
    calculate_batting_vs_left_rating(df1, batting_weights)
    calculate_batting_vs_right_rating(df1, batting_weights)
    calculate_baserunning(df1)
    calculate_catcher_defense(df1, defense_weights)
    calculate_infield_defense(df1, defense_weights)
    calculate_outfield_defense(df1, defense_weights)
    calculate_pitching_overall(df1, pitching_weights)
    calculate_pitching_vs_left(df1, pitching_weights)
    calculate_pitching_vs_right(df1, pitching_weights)

    df2 = df1[columns_to_keep]
    del df1
    return df2


def calculate_batting_overall_rating(df, weights):
    df['BatOA'] = (
            (df['BABIP'] * weights['BABIP']) +
            (df['Avoid Ks'] * weights['Avoid Ks']) +
            (df['Gap'] * weights['Gap']) +
            (df['Power'] * weights['Power']) +
            (df['Eye'] * weights['Eye'])
    )

def calculate_batting_vs_left_rating(df, weights):
    df['BatvL'] = (
        (df['BABIP vL'] * weights['BABIP vL']) +
        (df['Avoid K vL'] * weights['Avoid K vL']) +
        (df['Gap vL'] * weights['Gap vL']) +
        (df['Power vL'] * weights['Power vL']) +
        (df['Eye vL'] * weights['Eye vL'])
    )

def calculate_batting_vs_right_rating(df, weights):
    df['BatvR'] = (
        (df['BABIP vR'] * weights['BABIP vR']) +
        (df['Avoid K vR'] * weights['Avoid K vR']) +
        (df['Gap vR'] * weights['Gap vR']) +
        (df['Power vR'] * weights['Power vR']) +
        (df['Eye vR'] * weights['Eye vR'])
    )

def calculate_baserunning(df):
    df['BSR'] = df['Speed'] + df['Steal Rate'] + df['Stealing'] + df['Baserunning']

def calculate_catcher_defense(df, weights):
    df['Catch Def'] = (
        (df['CatcherAbil'] * weights['CatchAbil']) +
        (df['CatcherFrame'] * weights['CatchFrame']) +
        (df['Catcher Arm'] * weights['CatchArm'])
    )

def calculate_infield_defense(df, weights):
    df['IF Def'] = (
        (df['Infield Range'] * weights['IF Range']) +
        (df['Infield Error'] * weights['IF Error']) +
        (df['Infield Arm'] * weights['IF Arm']) +
        (df['DP'] * weights['DP'])
    )

def calculate_outfield_defense(df, weights):
    df['OF Def'] = (
        (df['OF Range'] * weights['OF Range']) +
        (df['OF Error'] * weights['OF Error']) +
        (df['OF Arm'] * weights['OF Arm'])
    )

def calculate_pitching_overall(df, pitching_weights):
    df['PitOA'] = (
        (df['Stuff'] * pitching_weights['Stuff']) +
        (df['pHR'] * pitching_weights['pHR']) +
        (df['pBABIP'] * pitching_weights['pBABIP']) +
        (df['Control'] * pitching_weights['Control'])
    )

def calculate_pitching_vs_left(df, pitching_weights):
    df['PitvL'] = df['Stuff vL'] + df['pHR vL'] + df['pBABIP vL'] + df['Control vL']

def calculate_pitching_vs_right(df, pitching_weights):
    df['PitvR'] = df['Stuff vR'] + df['pHR vR'] + df['pBABIP vR'] + df['Control vR']



