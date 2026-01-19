import sys
import pandas as pd

print('arguments', sys.argv)

month = sys.argv[1]

rows = pd.DataFrame({"A": [1,2], "B": [3,4]})
print(rows.head())
rows.to_parquet(f'output{month}.parquet')

pd.DataFrame()
print(f'hello pipeline, month = {month}')
