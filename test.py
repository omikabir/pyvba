import pyvba.fn as fun  
import pandas as pd
import numpy as np

xlfile = 'myfile.xlsx' 
df = pd.read_excel(xlfile, sheet_name = "RAW")
df1 = fun.countifs(df,df['Node'],df['Node'])
print("new column name cnt added at last of your dataframe \n", df1)
df2 = fun.countifs(df,df['Node'],"BHSDR07")
print("count of will be printed for provided string BHSDR07\n", df2)