"""Scripts to return df with batter ratings."""
import pandas as pd


def get_batter_ratings(file_path, passed_cid):
    df1 = pd.DataFrame(pd.read_csv(file_path))
    print("Passed cid: ", passed_cid)
    df1 = df1.rename(columns={'Card ID' : 'CID', '//Card Title':'Title', 'Card Value':'Val'})
    df1 = df1[df1['CID'] == int(passed_cid)][['CID', 'Title', 'Val', 'Bats', 'Throws', 'Contact', 'Gap', 'Power', 'Eye', 'Avoid Ks', 'BABIP']]

    return df1