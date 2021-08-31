import inspect
from datetime import datetime

import pandas as pd
import numpy as np
from haversine import haversine, Unit

from numpy import cos, sin, arcsin, sqrt
from math import radians

# # Understanding chaining and indexing in pandas
# # Define a dictionary containing ICC rankings
# rankings = {'test': ['India', 'South Africa', 'England',
#                      'New Zealand', 'Australia', 'Syria', 'Palestine'],
#             'odi': ['England', 'India', 'New Zealand',
#                     'South Africa', 'Pakistan', 'Mozambik', 'Nambia'],
#             't20': ['Pakistan', 'India', 'Australia',
#                     'England', 'New Zealand', 'Popua Neugeniea', 'Japan']}
#
# # Convert the dictionary into DataFrame
# rankings_pd = pd.DataFrame(rankings)
# print(rankings_pd)
#
# indexing = rankings_pd[1:5]
# print('\n' + "This is the result of indexing [1:5]")
# print(indexing)
#
# chaining = rankings_pd[1:5][1:3]
# print('\n' + "This is the result of chaining [1:5][1:3]")
# print(chaining)
#
# # Understanding first last valid index
# # Creating a dataframe
# df = pd.DataFrame({
#     'A': [np.NaN, 1, np.NaN, 3, np.NaN],
#     'B': [1, np.NaN, np.NaN, np.NaN, np.NaN]
# })
# print(df)
#
# # first valid index for each column
# first_index = df.apply(pd.Series.first_valid_index)
# print(first_index)
#
# # last valid index for each column
# last_index = df.apply(pd.Series.last_valid_index)
# print(last_index)
#
# # Understanding how to remove rows after a certain index using df.iloc
# mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
#           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
#           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000},
#           {'a': 44, 'b': 45, 'c': 46, 'd': 47},
#           {'a': 55, 'b': 56, 'c': 57, 'd': 58}]
#
# df = pd.DataFrame(mydict)
# print(df)
#
# # Sclicing before the second row (index 3)
# print(df.iloc[3:])
#
# # Slicing after the second row (index 3)
# print(df.iloc[:3])
#
# # Understanding checking the type of a column in pandas dataframe
# df_type_check = pd.DataFrame({"A": [1, 2, 'test', 4, 5], "B": ['a', 'b', 'c', 'd', 'e'],
#                               "C": ['b', 'a', 'c', 'c', 'd'], "D": ['a', 'c', 7, 9, 2]})
# # get the type of the entries of your column with map:
# print(df_type_check['A'].map(type))
# # filter on all values, which are not stored as int
# df_type_check['A'].map(type) != str


# # Understanding iterating over rows in a dataframe
# # dictionary of lists
# dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score': [90, 40, 80, 98]}
#
# # creating a dataframe from a dictionary
# df = pd.DataFrame(dict)
# print(df)
# # iterating over rows using iterrows() function
# for i, j in df.iterrows():
#     print(i, j)
#     print()

# #Getting the source code in python
# source_code = inspect.getsource('Objectname.functionname)
# print(source_code)


dict_time_lat_lon = {
    'time': ["2021-04-01 12:57:14", "2021-04-02 12:57:14", "2021-04-03 12:57:14", "2021-04-04 12:57:14"],
    'longitude': [119.7, 123.56666666666666, 122.92833333333333, 24.89666666666667],
    'latitude': [32.266666666666666, 30.15, 32.45, 45.77]}

df2 = pd.DataFrame(dict_time_lat_lon)

print(type(df2['time'][1]))


# df2['lat_diff'] = np.deg2rad(df2['latitude'].diff())
# df2['lon_diff'] = np.deg2rad(df2['longitude'].diff())
# print(df2)

# source_code = inspect.getsource(df2.diff)
# print(source_code)
#
# # iterating over rows using iterrows() function
# for i, j in df2.iterrows():
#     print(j[1], j[2])

# for i, j in df2.iterrows():
#     loc = (j[2], j[1])
#     print(loc)

# # This works!!!!!!
for index in range(len(df2) - 1):
    loc1 = df2['latitude'][index], df2['longitude'][index]
    loc2 = df2['latitude'][index + 1], df2['longitude'][index + 1]
    # print(loc1)
    # print(loc2)
    #
    # print()
    print(haversine(loc1,loc2,unit=Unit.METERS))

# # To print all elements in a serties in Pandas
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df.iloc[0])
