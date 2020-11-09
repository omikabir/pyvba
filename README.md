# pyvba
an attempt to wrap vba functions to python pandas. this is a mini reference with few pre build functions library that writen to use like excel vba functions

## Requirments:
**Basic knowledge about python programing (especially python datatype, dictionary, list, conditional, loop , function and lambda function) is good to go. if not, look through the project will give basic ideas about working priciples**

## Content:
- basic understanding and examples of approches
- essential pandas functions and usage
- examples of data and datatype conversion 
- usage example of pre build functions

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

result_dataframe = concat(mydataframe,"name_of_column1","name_of_column_x","new_column_name")
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

## pandas essential functions and usage
like **autofil** in excel VBA, pandas most of functions won't need to apply through loop.

### table for visualizing and testing

<table border="2">
  <th>PRODUCT</th>
  <th>ZIPCODE</th>
  <th>SHIPMENT</th>
  <th>DELIVERY</th>
  <th>PRICE</th>
  <th rowspan="10" colspan="2">
    <details><summary>CLICK TO SEE TABLE CODE</summary>
<p>

###### Copy & Paste should work

```python
import pandas as pd
df = pd.DataFrame([['Iphone','DHDEM26',
'11-09-2020 12:14','11-20-2020 12:24',
'400'],['Iphone','CGHTZ09',
'11-09-2020 12:14','11-20-2020 12:24',
'400'],['dell','LXRGN32',
'11-09-2020 12:14','11-20-2020 12:24',
'300'],['dell','LXRGN31',
'11-09-2020 12:13','11-20-2020 12:24',
'300'],['Samsung ','SGSJP04',
'11-09-2020 12:12','11-20-2020 12:24',
'250'],['Samsung ','CXMHK36',
'11-09-2020 12:11','11-20-2020 12:24',
'250'],['Samsung ','CGFTK29',
'11-09-2020 12:10','11-20-2020 12:24',
'250'],['dell','CGKTLB6',
'11-09-2020 12:10','11-20-2020 12:24',
'300'],['dell','CMBRR57',
'11-09-2020 12:10','11-20-2020 12:24',
'300']],columns=('PRODUCT','ZIPCODE',
            'SHIPMENT','DELIVERY','PRICE'))
print(df)
```

</p>
</details>
  </th>
<tr><td>Iphone</td><td>DHDEM26</td><td>11-09-2020 12:14</td><td>11-20-2020 12:24</td><td>400</td></tr>
<tr><td>Iphone</td><td>CGHTZ09</td><td>11-09-2020 12:14</td><td>11-20-2020 12:24</td><td>400</td></tr>
<tr><td>dell</td><td>LXRGN32</td><td>11-09-2020 12:14</td><td>11-20-2020 12:24</td><td>300</td></tr>
<tr><td>dell</td><td>LXRGN31</td><td>11-09-2020 12:13</td><td>11-20-2020 12:24</td><td>300</td></tr>
<tr><td>Samsung </td><td>SGSJP04</td><td>11-09-2020 12:12</td><td>11-20-2020 12:24</td><td>250</td></tr>
<tr><td>Samsung </td><td>CXMHK36</td><td>11-09-2020 12:11</td><td>11-20-2020 12:24</td><td>250</td></tr>
<tr><td>Samsung </td><td>CGFTK29</td><td>11-09-2020 12:10</td><td>11-20-2020 12:24</td><td>250</td></tr>
<tr><td>dell</td><td>CGKTLB6</td><td>11-09-2020 12:10</td><td>11-20-2020 12:24</td><td>300</td></tr>
<tr><td>dell</td><td>CMBRR57</td><td>11-09-2020 12:10</td><td>11-20-2020 12:24</td><td>300</td></tr>
</table>

#### filtering , remove duplicate , sorting
```
#filtering by partial string Match
    df1 = df[df.PRODUCT.str.contains('del')]
    df2 = df[df.PRODUCT.str.contains('del') & df.ZIPCODE.str.contains('LXRGN')]
    df3 = df[df.PRODUCT.str.contains('del') | df.ZIPCODE.str.contains('LXRGN')]

#filtering by Exact string Match




```