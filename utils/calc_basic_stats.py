import pandas as pd
import numpy as np

def calc_basic_stats(df):
    print('Calculating basic stats')
    print(df.head())
    df1 = pd.DataFrame(df)

    df2 = pd.DataFrame(df1)
    df2 = df2.groupby(['CID'], as_index=False)[['PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'IBB',
                                                'BB', 'HP', 'SH', 'SF', 'SO', 'TB', 'RC', 'WAR', 'SB',
                                                'CS', 'BsR', 'ZR']].sum()
    df2['AVG'] = (df2['H']/df2['AB']).round(3)
    df2['OBP'] = ((df2['H'] + df2['BB'] + df2['HP'])/(df2['AB'] + df2['BB'] + df2['HP'] + df2['SF'])).round(3)

    df3 = df2[df2['PA']>0][['CID', 'PA', 'AVG', 'OBP']]
    df3['CID'] = df3['CID'].astype(str)
    df3['PA'] = df3['PA'].astype(str)
    df3['AVG'] = df3['AVG'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")
    df3['OBP'] = df3['OBP'].apply(lambda x: f"{x:.3f}"[1:] if x < 1 else f"{x:.3f}")


    return df3