# pyvba
an attempt to wrap vba functions to python pandas with an intension to compile vba procedure into python. this is a guide with few pre build functions especially for vba developer

## Requirments:
**Basic knowledge about python programing (especially python datatype, dictionary, list, conditional, loop , function and lambda function)**

## Content:
- basic understanding about methods and approch
- usage guideline for pre build functions

## primary difference between excel and pandas dataframe

*number of columns: in excel there are 16382 columns in every sheet so we can use any column from that but dataframe columns are bound to data and we have to create new column every time while it needs, in following ways we can create new column*
```
df = df.assign(new_column = "NA")     #column inserted at last, here new_column = column name and "NA" = rows value of new column
df.insert(1, 'new-column', "NA", allow_duplicates=False)   #column inserted by index number, here 1 = index number
```
## ways to interpreat excel vba into python padas dataframe

generally, in vba, a formula/condition can be applied on column 
1. using for loop
2. using autofill

### lets, concat 2 column and store data into a new column of a dataframe
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


#### Approch 1:


### Approch 2:
