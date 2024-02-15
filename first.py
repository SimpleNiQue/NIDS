import pandas as pd
df = pd.read_csv("Train_data.csv")

        # Get the column headers and store them in a list
column_headers = list(df.columns)
print(column_headers)