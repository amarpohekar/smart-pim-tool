'''
@File  : sample_data_template.py
@brief : In this file have extraction of column name in tamplete by using pandas liabrary.
'''

import pandas as pd


df = pd.read_excel('sample_data.xlsx


df[1].to_excel("list_column.xlsx")




df2 = pd.read_excel('sample_data.xlsx',sheet_name='page-2-table-1',index_col=0)




print(df2)


)

df2.loc[0].to_excel('list_column1.xlsx')




data= pd.read_excel('list_column.xlsx')





print(data)





data1=pd.read_excel('list_column1.xlsx')





print(data1)





data_column=pd.concat([data,data1])





print(data_column)





data_column.to_excel('Sample_column.xlsx')







