# pyvba
an attempt to wrap vba functions to python pandas with an intension to compile vba procedure into python. this is a guide with few pre build functions especially for vba developer

## Requirments:
**Basic knowledge about python programing (especially python datatype, dictionary, list, conditional, loop , function and lambda function)**

## Content:
- basic understanding and example of approches
- essential convertion methods

## primary difference between excel and pandas dataframe

**number of columns:** in excel there are 16382 columns in every sheet so we can use any column from that during calculation but dataframe columns are bound to data and we have to create new column every time while it needs, in following ways we can create new column
```
df = df.assign(new_column = "NA")     #column inserted at last, here new_column = column name and "NA" = rows value of new column
df.insert(1, 'new-column', "NA", allow_duplicates=False)   #column inserted by index number, here 1 = index number
```
## ways to interpreat excel vba into python padas dataframe

in vba, a formula/condition can be applied on column using for loop where data can be referenced in 2 ways
1. only cell as ref (vba function **instr/datediff** use cell wise reference) 
2. cell + range both used as ref (vba function **countif/match** use both, cell and range as reference)

### approch where, only cell used as ref. lets concat 2 columns of dataframe and store value into a new column using for loop similar to vba for loop
```
using vba like **For loop**

def concat(df, column_1, column_2, new_column_name):      #column_1 and conlumn_2 represent column header name
    df = df.assign(new_column = "NA")
    df.rename(columns = {'new_column': new_column_name}, inplace = True)
    for i in range(len(df)):
        data_1 = df.loc[i,column_1]       #df.iloc[i,column_1] (if column_1 is index number like 1/2/3...]
        data_2 = df.loc[i,column_2]
        df.loc[i,new_column_name] = str(data_1) + str(data_2)
    return df

using **pandas method**
  df['new_column_name'] = df['column_1'].str.cat(df['column_2'])
```

### approch where, cell + range both used as ref. lets implement countif function for dataframe
in vba countif function can be written as **application.countif(range("A2"),range("A:A"))**, we can apply this function using for loop to get count of all cells value in column A & can store the value in column B. for dataframe it can be implement as following
```
#copy and paste in your IDE to check the result

import pandas as pd

def countif(col_as_range,criteria):
    # col_as_range can be list or daraframe series
    if isinstance(col_as_range,list):
        count = col_as_range.count(criteria)
        return count
    elif isinstance(col_as_range, pd.core.series.Series):
        col_range_list = col_as_range.values.tolist()
        count = col_range_list.count(criteria)
        return count
    else:
        return "none"

# way of calling - print(countif(df['Colname'],"value_to_check"))
# we call above countif function using loop on dataframe and can store the result into a new column as following.

df = pd.DataFrame({
    'column_1': ['g', 't', 'n', 'w', 'n', 'g']
})

df = df.assign(new_column = "NA")
list_as_range = df['column_1'].values.tolist()   #column_1 is the column name (can be any column)
for i in range(len(df)):
    cell_value = df.loc[i,'column_1']   #column_1 is the column name (can be any column)
    df.loc[i,'new_column'] = countif(list_as_range, cell_value)   #calling above functions

print(df)
```
