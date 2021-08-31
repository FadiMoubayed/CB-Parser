from math import radians
import pandas as pd
import numpy as np
import pyproj

from haversine import haversine, Unit

df_test = pd.DataFrame({'city': ['bangalore', 'Mumbai', 'Delhi', 'kolkatta', 'chennai', 'bhopal'],
                        'latitude': [12.9716, 19.076, 28.7041, 22.5726, 13.0827, 23.2599],
                        'longitude': [77.5946, 72.877, 77.1025, 88.639, 80.2707, 77.4126], })

# df['lat'] = np.radians(df['lat'])
# df['lon'] = np.radians(df['lon'])

# print(df_test)


print(df_test[["latitude", "longitude"]] - df_test[["latitude", "longitude"]].shift(1))

print(type(df_test[["latitude", "longitude"]] - df_test[["latitude", "longitude"]]))

# for index in range(len(df_test) - 1):
#     loc1 = df_test['latitude'][index], df_test['longitude'][index]
#     loc2 = df_test['latitude'][index + 1], df_test['longitude'][index + 1]
#     distance = haversine(loc1, loc2, unit=Unit.KILOMETERS)
#     # print(loc1)
#     # print(loc2)
#     print(distance)

# print(haversine(loc1,loc2,unit=Unit.KILOMETERS))
#
# df_test['distance'] = haversine(loc1, loc2, unit=Unit.KILOMETERS)
# print(df_test)

pd.set_option('display.max_columns', None)


# Approach 1:
# Creates a list within the function
def calculate_distance(df):
    # This creates a list with a first element of 0 because the first row of coordinates does not result in distance
    distance = [0, ]
    for index in range(len(df) - 1):
        loc1 = df['latitude'][index], df['longitude'][index]
        loc2 = df['latitude'][index + 1], df['longitude'][index + 1]
        distance.append(haversine(loc1, loc2, unit=Unit.KILOMETERS))
    return distance


# Adds the distance column to the dataframe
df_test['distance'] = calculate_distance(df_test)

lat1 = 0.5606666666666666
lon1 = 45.003166666666665
lat2 = 0.5636666666666666
lon2 = 45.00366666666667


fwd_azimuth = pyproj.Geod(ellps='WGS84').inv(lon1, lat1, lon2, lat2)
print(fwd_azimuth[0])
print(type(fwd_azimuth))


# test_distance = haversine(lat1, lon1, lat2, lon2)
# print(test_distance)

# TRYING TO USE LAMBDAS - DOES NOT WORK!!!
# def calculate_distance(df):
#     loc1 = df['latitude'], df['longitude']
#     loc2 = df['latitude'].shift(1), df['longitude'].shift(1)
#     distance = haversine(loc1, loc2, unit=Unit.KILOMETERS)
#     return distance
#
# #
# df_test.insert(loc=2, column='distance',
#                 value=df_test.apply(lambda df: calculate_distance(df),
#                                     axis=1))


# df_test.insert(loc=2, column='distance',
#               value=df_test.apply(lambda col: calculate_distance,
#                              axis=1))
#
# print(df_test)
