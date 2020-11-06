# pyvba
an attempt to wrap vba functions to pandas dataframe. This might be useful to convert vba project/excel macro in python

##### new column: in vba we don't have to worry about new column, but in dataframe we have to.
we can create new columns in dataframe in following approch. following **add_col_df** function can be used to create new columns in dataframe.
add_col_df(df, "column_10", "NA", 5)
df = dataframe to add column, column_10 = name of new column in string
"NA" = columns values for all rows (optional), 5 = index number for inserting a column if omitted, column will be created at last.
```
df = df.assign(new_column = "NA")     #column inserted at last, here new_column = column name and "NA" = rows value of new column
df.insert(1, 'new-column', "NA", allow_duplicates=False)   #column inserted by index number, here 1 = index number
```
##### for loop: after creating a new column, these column can be used to store new value which generally derived from existing column or can be map/vlookup with others
