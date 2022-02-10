'''
@File  : sample_data_template.py
@brief : In this file have extraction of column header in 
         list format from "sample_data.xlsx" by using pandas liabrary.
'''

from tkinter import filedialog
import tkinter as tk
import pandas as pd

'''
@function : sample_column_header(filepath)
@brief    : this function gives all column header in excel file
@param    :  
@return   : this will gives column header
'''
def sample_column_header():
    try:
        root = tk.Tk() 
        filepath = filedialog.askopenfilename()
        root.destroy()
        df = pd.read_excel(filepath)
        list1 = list(df[1])
        df1 = pd.read_excel(filepath,sheet_name=1)
        df1.columns=list("ABCDEFG")
        newdf = df1.drop(["A"],axis=1)
        list2 = list(newdf.loc[0])
        list1.extend(list2)
        print("columns header list :- ")
        print(list1)
        return list1
    except:
        print("Error in Execution")


'''
@function : load_template_header(filepath)
@ brief   : this function gives all column header in excel file
@param    :  
@return   : this will gives column header
'''

def load_template_header():
    try:
        root = tk.Tk()
        filepath = filedialog.askopenfilename()
        root.destroy()
        data = pd.read_excel(filepath)
        list2 = list(data.columns)
        print("column header list :- ")
        print(list2)
        return list2
    except:
        print("Error in Execution")


