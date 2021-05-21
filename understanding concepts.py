import pandas as pd
import numpy as np

# Understanding chaining and indexing in pandas
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia','Syria','Palestine'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan','Mozambik','Nambia'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand','Popua Neugeniea','Japan']}

# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
print(rankings_pd)

indexing = rankings_pd[1:5]
print('\n' + "This is the result of indexing [1:5]")
print(indexing)

chaining = rankings_pd[1:5][1:3]
print('\n' + "This is the result of chaining [1:5][1:3]")
print(chaining)

# Understanding first last valid index
# Creating a dataframe
df = pd.DataFrame({
    'A': [np.NaN, 1, np.NaN, 3, np.NaN],
    'B': [1, np.NaN, np.NaN, np.NaN, np.NaN]
})
print(df)

# first valid index for each column
first_index = df.apply(pd.Series.first_valid_index)
print(first_index)

# last valid index for each column
last_index = df.apply(pd.Series.last_valid_index)
print(last_index)