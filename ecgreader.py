import pandas as pd

records = pd.read_csv('records_names.csv', header=None, squeeze=True, index_col=0)
