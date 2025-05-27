"""Process raw files into ready data file."""
import os
import pandas as pd
import glob


"""Process files into the ready CSV."""


def process_files(self, target_csv, raw_dir):
    """Process files into the ready CSV."""
    target_csv = target_csv
    raw_dir = raw_dir

    print(f"Target CSV: {target_csv}")
    print(F"Raw CSV: {raw_dir}")

    def cull_teams(df):
        df1 = pd.DataFrame(df)
        teams = pd.DataFrame(df1[['ORG', 'GS.1', 'R']].groupby(['ORG']).sum())
        teams['R/G'] = teams['R']/teams['GS.1']
        teams_out = teams[teams['R/G'] > 8]
        teams_out = teams_out.reset_index()
        df1_filtered = df1[~df1['ORG'].isin(teams_out['ORG'])]
        return df1_filtered

    def add_file(target_file, file_to_add):
        file_name_string = os.path.splitext(os.path.basename(file_to_add))[0]
        addition = cull_teams(pd.read_csv(file_to_add))
        addition['Trny'] = file_name_string

        if target_file.empty or target_file.isna().all().all():
            return addition
        else:
            return pd.concat([target_df, addition])

    target_df = pd.read_csv(target_csv)
    num_files_added = 0
    existing_files = set(target_df['Trny'].unique())

    # update the file with each file in the directory
    for file_path in glob.glob(os.path.join(raw_dir, '*.csv')):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        if file_name not in existing_files:
            target_df = add_file(target_df, file_path)
            print(file_name)
            num_files_added += 1

    target_df.to_csv(target_csv, index=False)
    print(f"Processed {num_files_added} files")
