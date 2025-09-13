import pandas as pd
import glob

# Get list of all CSV files in the data folder
csv_files = glob.glob('data/*.csv')

# Read and concatenate all files into one DataFrame
df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
print()

df = df[df['product'] == 'Pink Morsel']

df['sales'] = df['price'] * df['quantity']

df = df[['sales', 'date', 'region']]

df.to_csv('.data/daily_sales_data_pinkMorsel.csv', index=False)