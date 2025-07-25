"""Check for teams to remove due to outlier statistics."""


def cull_teams(df):
    """Cull teams that have more than the given number of runs."""
    team_stats = df.groupby(['ORG', 'Trny'],
                            as_index=False)[['GS.1', 'R']].sum()
    team_stats['R/G'] = team_stats['R'] / team_stats['GS.1']

    # Identify teams to remove
    teams_ok = team_stats.loc[team_stats['R/G'] < 8, ['ORG', 'Trny']]

    # Merge to flag rows to drop
    df1_filtered = df.merge(teams_ok, on=['ORG', 'Trny'], how='inner')
    removed_count = len(df) - len(df1_filtered)

    return df1_filtered, removed_count
