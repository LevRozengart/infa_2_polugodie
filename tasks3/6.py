import pandas as pd
import glob
import os

def merge_csvs(directory):
    pattern = os.path.join(directory, '*.csv')
    files = glob.glob(pattern)
    dataframes = []
    for f in files:
        data = pd.read_csv(f)
        dataframes.append(data)
    if not dataframes:
        print("No files to process.")
        return pd.DataFrame()
    combined_data = dataframes[0]
    for d in dataframes[1:]:
        combined_data = pd.merge(combined_data, d, on='user_id', how='outer')
    return combined_data
  
directory = './data/'
merged_data = merge_csvs(directory)
print(merged_data.to_string()
