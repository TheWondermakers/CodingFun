import os
import pandas as pd


# Load the dataset
cwd = os.getcwd()  # Get current working directory
csv_path_baselist = os.path.join(cwd, 'python/data', 'baselist.csv')
df_baselist = pd.read_csv(csv_path_baselist)
csv_path_agribalyse = os.path.join(cwd, 'python/data', 'agribalyse.csv')
df_agribalyse = pd.read_csv(csv_path_agribalyse)

print(df_baselist.head())
print(df_agribalyse.head())


# TODO: Input your code here
