import pandas as pd

data_path = 'data.txt'

df = pd.read_csv(data_path, sep='\s+', index_col=0)

print(df)
