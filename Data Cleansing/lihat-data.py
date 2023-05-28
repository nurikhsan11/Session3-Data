import pandas as pd
pd.options.display.max_columns = 50
# Importing Data Source
df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')
print(df_load.shape)
print(df_load.head(5))
print(df_load.customerID.nunique())