# CB-Parser
Parses Carl Büttner's data Excel sheets and converts them to csv format

## Procedure
+ Read the Excel sheet as a dataframe using Pandas and properly rename the columns (Remove the spaces)
+ Get the first valid value of the first column. This value is used to remove the empty rows at the beginning of the dataframe
+ Drop the NA values in the dataframe and only keep the valid values
+ Save the result to a csv file

## Second parser
+ Converts the latitude and longitude from degrees-minutes-seconds to degrees
+ Calculates distance between each set of coordinates using the haversine formula using the following function:

    https://pypi.org/project/haversine/

+ Calculates the speed of the ship between each set of coordinates in kilometers per hour
+ Calculates the bearing in degrees between each set of coordinates using the following function:

    https://pyproj4.github.io/pyproj/stable/api/geod.html#pyproj-geod

## How to use
In terminal type:

    python3 name_of_the_script.py path_to_excel_files

Example:

    python3 parse_excel_files.py ./Excel_Files/


