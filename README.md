# CB-Parser
Parses Carl Büttner's data Excel sheets and converts them to csv format

## Procedure
+ Read the Excel sheet as a dataframe using Pandas and properly rename the columns (Remove the spaces)
+ Get the first valid value of the first column. This value is used to remove the empty rows at the beginning of the dataframe
+ Drop the NA values in the dataframe and only keep the valid values
+ Save the result to a csv file

## How to use
+ Add a folder Excel_Files to the working directory
+ Load the desired file into the folder Excel_Files
+ Provide the name of the file that is to be converted into csv in the variable "file_name"
+ The result is saved (!!!!!!! Still need to work on this !!!!!!!!!!!)
