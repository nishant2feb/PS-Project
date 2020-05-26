# Task 1: Importing Pandas library
import pandas as pd

# Task 2: Reading CSV file "Code.csv" into a Pandas DataFrame
df1 = pd.read_csv('data/Code.csv')

# Task 3: Reading CSV file "ISOnum.csv" into a Pandas DataFrame
df2 = pd.read_csv('data/ISOnum.csv')

# Task 4: Merging two dataframes On Country column as CountryCode
CountryCode = pd.merge(df1, df2, on = 'country')

