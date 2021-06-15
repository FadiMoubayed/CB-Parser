import pandas as pd
import os

# TODO: Clean the unnecessary prints

# TODO: add a message when the file has been read and converted successfully.

# Providing file info

# Providing the file name
file_name = "CB PACiFIC_TEF30_2021 up to 08 April.xls"
# providing the file relative path
# Is this a good way to provide that file path or should I use os.path.relpath??
file_path = './Excel_Files/' + file_name
# providing the file sheet that will be read
file_sheet = "Daily general"

# Trying to add try
try:
    # Listing the sheets available in the Excel file
    xl = pd.ExcelFile(file_path)
    sheet_names = xl.sheet_names
    # print("The sheets available in this excel file '" + file_name + "' are: " + '\n')
    # print(*sheet_names, sep='\n')

    # providing the final column names
    # names = ['time_period_start',
    #          'time_period_end',
    #          'wind_direction_degree',
    #          'wind_speed_km',
    #          'swell_direction_degree',
    #          'swell_height_km',
    #          'seascale_beaufort_scale',
    #          'current_direction_degree',
    #          'current_speed_kt',
    #          'draft_fwd_m',
    #          'draft_aft_m',
    #          'mean_draft_m',
    #          'trim_m',
    #          'ballast_quantity_cbm',
    #          '_ttl_displacement_mt',
    #          'remarks']

    # Using a dictionary instead of a list. The keys will be used to rename the columns and the values will be used
    # for assigning each column's data type later.
    # TODO: check why assigning the data type int is not working. I also tried int64 and it is not working either.
    names_dic = {
        'time_period_start': 'datetime64',
        'time_period_end': 'datetime64',
        'wind_direction_degree': 'int',
        'wind_speed_km': 'int',
        'swell_direction_degree': 'float',
        'swell_height_km': 'float',
        'seascale_beaufort_scale': 'str',
        'current_direction_degree': 'float',
        'current_speed_kt': 'float',
        'draft_fwd_m': 'float',
        'draft_aft_m': 'float',
        'mean_draft_m': 'float',
        'trim_m': 'float',
        'ballast_quantity_cbm': 'float',
        '_ttl_displacement_mt': 'float',
        'remarks': 'str'
    }

    # reading the excel file
    df = pd.read_excel(file_path, sheet_name=file_sheet, names=names_dic.keys())
    # Printing the default types after reading the file
    # print('the default types after reading the file')
    # print(df.dtypes)


    # Getting the unique values of a column
    print(df['seascale_beaufort_scale'].unique())
    # Getting the unique values for each column
    unique_values = df.apply(lambda column: column.unique())
    print('The unique values for each column in the dataframe: ')
    print(unique_values)

    # # TODO: Check why float is returned as the index and not integer!

    # I am not sure why the values' type here is float and not integer. Changing the data type did not work

    # Getting the first non Na index in each column

    # In this section the first 2 lines that are either empty or contain the units are removed
    # Since the columns are renamed, the index starts from the row next to the column names (That's why it starts at 2)

    first_notna_index = df.apply(pd.Series.first_valid_index)
    # print('\n' + "The first index is")
    # print(first_notna_index)
    #
    # print("The first value of the not na series")
    # print(int(first_notna_index[0]))

    # # dropping the null rows based on the first valid value of the first column (after removing the first three rows)
    df_3 = df.iloc[int(first_notna_index[0]):]


    # TODO: use dropna instead of the last value.

    # I think it is better to use the last value of the first column instead of dropna for the following reasons:
    # 1- using the option any in dropna is removing everything.
    # 2- using the option all is not removing anything.
    # df_final = df_3.dropna(how='any')

    # getting the last non Na index
    last_notna_index = df_3.apply(pd.Series.last_valid_index)
    # print('\n' + "The last index is")
    # print(last_notna_index)

    # TODO: Check why it is leaving an extra empty line ( with empty values) in the end. Could be solved by adding -2
    #  (-2 for the extra line that the first line already has
    df_final = df_3.iloc[:int(last_notna_index[0]) -2]

    # TODO: assigning the datatypes like this is resulting in an error because there are still NA values
    # # Assigning the data types for each column
    df_final.astype(names_dic.values())

    # Checking the datatypes after assigning them
    print(df_final.dtypes)


    # df_final.astype(names_dic)
    # print(df_final)

    df_3.to_csv("output_csv", encoding='utf-8', index=False)
    df_final.to_csv("output_csv_final", encoding='utf-8', index=False)

    datatype = df_final.dtypes
    print(datatype)

# If the file does not exist, the user gets a message and the files avialble in the directory Excel_Files are listed
except FileNotFoundError:
    print("File does not exsit! Make sure the directory Excel_Files exists and double check the file's name")
    print("Files available in the 'Excel_Files' directory are:")
    print(os.listdir('./Excel_Files/'))


# # TODO: change the name of the output csv file to match the name of the original file.
# # TODO: change the output to an output folder
# # TODO: make sure the values start at the same line (generic or hard coded?)
