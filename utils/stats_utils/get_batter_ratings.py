"""Scripts to return df with single batter ratings."""
import pandas as pd


def get_batter_ratings(file_path, passed_cid):
    """Return df with singular batter ratings."""
    df1 = pd.DataFrame(pd.read_csv(file_path))
    print("Passed cid: ", passed_cid)
    df1 = df1.rename(columns={'Card ID': 'CID',
                              '//Card Title': 'Title',
                              'Card Value': 'Val'})
    df1 = (df1[df1['CID'] == int(passed_cid)][[
        'CID', 'Title', 'Val', 'Bats', 'Throws', 'Gap',
        'Power', 'Eye', 'Avoid Ks', 'BABIP', 'BABIP vL',
        'Gap vL', 'Power vL', 'Eye vL', 'Avoid K vL',
        'BABIP vR', 'Gap vR', 'Power vR', 'Eye vR', 'Avoid K vR',
        'Speed', 'Steal Rate', 'Baserunning', 'Sac bunt',
        'Bunt for hit', 'CatcherAbil', 'CatcherFrame', 'Catcher Arm',
        'Infield Range', 'Infield Error', 'Infield Arm', 'DP',
        'OF Range', 'OF Error', 'OF Arm'
    ]])

    return df1
