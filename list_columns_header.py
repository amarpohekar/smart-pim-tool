'''
@File  : sample_data_template.py
@brief : In this file have extraction of column header in list format from "sample_data.xlsx" by using pandas liabrary.
'''

import pandas as pd


def column_header():
    df = pd.read_excel('sample_data.xlsx')
    list1 = list(df[1])
    df1 = pd.read_excel('sample_data.xlsx',sheet_name=1)
    df1.columns=list("ABCDEFG")
    newdf = df1.drop(["A"],axis=1)
    list2 = list(newdf.loc[0])
    list1.extend(list2)
    columns_header = list1
    print("columns header list :- ")
    print(columns_header)
    return 0





