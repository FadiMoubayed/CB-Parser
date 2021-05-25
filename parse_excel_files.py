import pandas as pd

# Providing file info

# Providing the file name
file_name = "CB PACiFIC_TEF30_2021 up to 08 April.xls"
# providing the file relative path
# Is this a good way to provide that file path or should I use os.path.relpath??
file_path = './Excel_Files/' + file_name
# providing the file sheet that will be read
file_sheet = "Daily general"

# Listing the sheets available in the Excel file
xl = pd.ExcelFile(file_path)
sheet_names = xl.sheet_names
print("The sheets available in this excel file '" + file_name + "' are: " + '\n')
print(*sheet_names, sep='\n')



names = ['time_period_start',
         'time_period_end',
         'wind_direction_degree',
         'wind_speed_km',
         'swell_direction_degree',
         'swell_height_km',
         'seascale_beaufort_scale',
         'current_direction_degree',
         'current_speed_kt',
         'draft_fwd_m',
         'draft_aft_m',
         'mean_draft_m',
         'trim_m',
         'ballast_quantity_cbm',
         '_ttl_displacement_mt',
         'remarks']

# reading the excel file
df = pd.read_excel(file_path, sheet_name=file_sheet, names=names)
# properly renaming columns

df.rename(columns={'Time period': 'time_period_start',
                   'Unnamed: 1': 'time_period_end',
                   'Wind': 'wind_direction_degree',
                   'Unnamed: 3': 'wind_speed_km',
                   'Swell': 'swell_direction_degree',
                   'Unnamed: 5': 'swell_height_km',
                   'Seascale': 'seascale_beaufort_scale',
                   # this has a space before
                   ' Current': 'current_direction_degree',
                   'Unnamed: 8': 'current_speed_kt',
                   'Draft': 'draft_fwd_m',
                   'Unnamed: 10': 'draft_aft_m',
                   'Mean draft': 'mean_draft_m',
                   'Trim': 'trim_m',
                   'Ballast': 'ballast_quantity_cbm',
                   'ttl displacement': '_ttl_displacement_mt',
                   'Remarks': 'remarks',
                   }, inplace=True)

# dropping the first three rows
df_3 = df.iloc[3:]

# Here it results in SettingWithCopyWarning
# renaming the columns of the dataframe
# df_3.rename(columns={'Time period': 'time_period_start',
#                      'Unnamed: 1': 'time_period_end',
#                      'Wind': 'wind_direction_degree',
#                      'Unnamed: 3': 'wind_speed_km',
#                      'Swell': 'swell_direction_degree',
#                      'Unnamed: 5': 'swell_height_km',
#                      'Seascale': 'seascale_beaufort_scale',
#                      'Current': 'current_direction_degree',
#                      'Unnamed: 8': 'current_speed_kt',
#                      'Draft': 'draft_fwd_m',
#                      'Unnamed: 10': 'draft_aft_m',
#                      'Mean draft': 'mean_draft_m',
#                      'Trim': 'trim_m',
#                      'Ballast': 'ballast_quantity_cbm',
#                      'ttl displacement': '_ttl_displacement_mt',
#                      'Remarks': 'remarks',
#                      }, inplace=True)

# getting the first non Na index
first_notna_index = df_3.apply(pd.Series.first_valid_index)
print('\n' + "The first index is")
print(first_notna_index)

# getting the last non Na index
last_notna_index = df_3.apply(pd.Series.last_valid_index)
print('\n' + "The last index is")
print(last_notna_index)

# writing the file to csv
df_3.to_csv("output_csv", encoding='utf-8', index=False)

# Checking the columns after being renamed
print(df_3.columns)
print(df_3.info())
print(df_3.head)
# print(df.iloc[0])
# print(df.iloc[1])
# print(df.iloc[2])
# print(df.iloc[3])

# print(df.head)
# print(df_3)


# # Getting the type of the object
# print(type(df))
# # Getting information about the read dataframe
# df.info()
# # Getting the columns of the dataframe
# result = df.columns
# print(result)
# # Getting the data types of the dataframe
# data_types = df.dtypes
# print(data_types)
# print(df.size)

# Getting the column Time period - first column
# time_period = df['Time period']
# print(time_period)
# Getting the column Time period - second column
# time_period_end = df['Unnamed: 1']
# print(time_period_end)


# def say_hello():
#     print("Hi Marzi! Num Num Num Num Num Num Num")
#
# say_hello()


# TODO: make sure the sheet exist in the file

# TODO: make sure the vlaues start at the same line (generic or hard coded?)
