"""Check for teams to remove due to outlier statistics."""
import pandas as pd


def cull_teams(df):
    """Cull teams that have more than the given number of runs."""
    df1 = pd.DataFrame(df)
    teams = df1.groupby(['ORG', 'Trny'])[['GS.1', 'R']].sum().reset_index()
    teams['R/G'] = teams['R'] / teams['GS.1']

    # Identify teams to remove
    teams_out = teams[teams['R/G'] > 8][['ORG', 'Trny']]

    # Merge to flag rows to drop
    df1 = df1.merge(teams_out, on=['ORG', 'Trny'], how='left', indicator=True)
    df1_filtered = df1[df1['_merge'] == 'left_only'].drop(columns=['_merge'])

    removed_count = len(df1) - len(df1_filtered)

    return df1_filtered, removed_count
