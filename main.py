import pyvba.fn as fx  
import pandas as pd


df = pd.DataFrame([['Iphone','DHDEM26','30-10-2020 12:14','25-11-2020 12:24','400'],['Iphone','CGHTZ09','11-09-2020 12:14','22-11-2020 12:24','400'],
['dell','LXRGN32','11-09-2020 12:14','19-11-2020 12:24','300'],['dell','LXRGN31', '11-09-2020 12:13','11-20-2020 12:24','300'],
['Samsung ','SGSJP04', '11-09-2020 12:12','11-20-2020 12:24','250'],['Samsung ','CXMHK36', '11-09-2020 12:11','11-20-2020 12:24','250'],
['Samsung ','CGFTK29', '11-09-2020 12:10','11-20-2020 12:24','250'],['dell','CGKTLB6','11-09-2020 12:10','11-20-2020 12:24','300'],
['dell','CMBRR57', '11-09-2020 12:10','11-20-2020 12:24','300']],columns=('PRODUCT','ZIPCODE','SHIPMENT','DELIVERY','PRICE'))


# https://www.online-python.com/vCLfOFiBI6
df0 = df # keeping original dataframe intact
dfn = df.convert_dtypes()       # covert full dataframe into string
dfn['PRICE'] = dfn['PRICE'].astype('int')   # can be 'int'/'object'/'float'
dfn['SHIPMENT'] = pd.to_datetime(dfn['SHIPMENT']) # convert into date fixed format ("%Y/%m/%d")
dfn['DELIVERY'] = pd.to_datetime(dfn['DELIVERY']) # convert into date fixed format ("%Y/%m/%d")
df = dfn

## filtering (partial string matching)
df1 = df[df.PRODUCT.str.contains('del')]
df2 = df[df.PRODUCT.str.contains('del') & df.ZIPCODE.str.contains('LXRGN')]
df3 = df[df.PRODUCT.str.contains('del') | df.ZIPCODE.str.contains('LXRGN')]

#filtering (Exact string Match)
lst = ['Iphone','dell']
df4 = df[df['PRODUCT'].isin(lst)]  # pick exact match from list of items
df5 = df[~df['PRODUCT'].isin(lst)] # pick except list of items
df6 = df[~df['PRODUCT'].isin(lst) & df['ZIPCODE'].isin(['LXRGN32'])] # conditional filtering


xlfile =('myfile.xlsx') 
newData = pds.read_excel(xlfile) 