# CB-Parser
Parses Carl Büttner's data Excel sheets and converts them to csv format

## Procedure
+ Read the Excel sheet as a dataframe using Pandas and properly rename the columns (Remove the spaces)
+ Get the first valid value of the first column. This value is used to remove the empty rows at the beginning of the dataframe
+ Drop the NA values in the dataframe and only keep the valid values
+ Save the result to a csv file

## How to use
In terminal type:

    python3 name_of_the_script.py path_to_excel_files

Example:

    python3 parse_excel_files.py ./Excel_Files/


