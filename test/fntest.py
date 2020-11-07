import sys
import pandas as pd
import pyvba.fnfn as fn
import numpy as np

pt1 = sys.path
mpath = pt1[1]
df0 = pd.read_csv (mpath + "//csvfile//100_Sales_Records.csv")
df1 = pd.read_csv (mpath + "//csvfile//items_price.csv")
df2 = pd.read_csv (mpath + "//csvfile//orders_details.csv")


class loop:
    def __init__(self, dfx, *args):
        self.df = dfx
        self.L = []
        self.ls = []
        self.lss = []
        for n in args:
            self.L.append (n)
        self.ndf = dfx.iloc[:,self.L]
        for i in range (self.df.shape[0]):
            for x in range (len (args)):
                try:
                    self.ls.append (self.df.loc[i, args[x]])
                except:
                    self.ls.append (self.df.iloc[i][args[x]])
            self.lss.append (self.ls)
            self.ls = []
        print (self.ndf)

    def instr(self, strtext, strsearch):
        for i in range (len (self.lss)):
            print ()

    # if isinstance (argvs[n], str):
    # print (df.loc[i, argvs[n]])
    # for i in range(len(df)):

class vbloop:
    def __init__(self, dfx, *args):
        self.mdf = dfx
        self.odf = dfx

    def getdf(self):
        return self.mdf

    def left(self, sdf, i):
        df1 = fn.add_col_df (self.mdf, 'left_apply')
        df1['left_apply'] = sdf.apply (lambda x: x[0:i])
        self.mdf = df1

    def right(self, sdf, i):
        df1 = fn.add_col_df (self.mdf, 'right_apply')
        df1['right_apply'] = sdf.apply (lambda x: x[-i:len (x)])
        self.mdf = df1

    def vlookup(self,sdf,refcol,pickcol=False):
        df1 = self.mdf.merge (sdf, on=refcol)
        self.mdf = df1

    def rmv_duplicates(self, *args):
        self.L = []
        for n in args:
            self.L.append (n)
        df1 = self.mdf.replace (r'^\s*$', np.nan, regex=True)
        df1 = df1.drop_duplicates (subset=self.L)
        self.mdf = df1

    def sort_dsc(self, oncol):
        df = self.mdf.replace (r'^\s*$', np.nan, regex=True)
        self.mdf = df.sort_values (by=oncol, ascending=False)

    def sort_asc(self, oncol):
        df = self.mdf.replace (r'^\s*$', np.nan, regex=True)
        self.mdf = df.sort_values (by=oncol, ascending=True)

    def map_df_dic(self, dic, refcol):
        nc = str(self.mdf.shape[1]+1)
        df = fn.add_col_df (self.mdf , nc)
        df[nc] = df[refcol].map (dic)
        self.mdf = df

    def concat(self,*argv):
        n = 0
        ls = []
        while n < len (argv):
            if isinstance (argv[n], pd.core.series.Series):
                if len (ls) <= 1:
                    ls = argv[n].to_list ()
                else:
                    ls0 = argv[n].to_list ()
                    ls1 = fn.aplist (ls, ls0)
                    ls = ls1
            n = n + 1
        nc = str (self.mdf.shape[1] + 1)
        df1 = fn.add_col_df (self.mdf, nc)
        df1[nc] = np.array (ls)
        self.mdf = df1

    def conv_datatype(self, colname, typ):
        if typ == 'date':
            self.mdf[colname] = pd.to_datetime (self.mdf[colname], errors='coerce')
        elif typ == 'int':
            print('x')
        elif typ == 'str':
            self.mdf[colname] = self.mdf[colname].applymap(str)


#ob = vbloop(df1)
#ob.left(df1['Item Type'],5)
#ob.right(df1['Item Type'],3)
#ob.concat(df1['Item Type'],df1['Unit Price'])
print(df0.columns)
df = fn.add_col_df(df0,'OM')
list_of_cols_as_ref = ['Region','Country','Item Type']
df['OM'] = df[list_of_cols_as_ref].apply(lambda x: ''.join(map(str,x)),axis=1)
print(df)
#df[st] = df[list_of_cols_as_ref].apply(lambda x: ''.join(map(str,x)),axis=1)
#print(ob.getdf())
## dL = fn.left (df1, df1['Item Type'], 3)
## dR = fn.right (df1, ddd = fn.right (df1, df1['Item Type'], 3)f1['Item Type'], 3)
