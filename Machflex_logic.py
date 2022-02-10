'''
@File  : funct_MF.py
@brief : this file contain varios function which will be used
'''
import os
from random import sample
from re import template
import tkinter as tk
from tkinter import filedialog
import camelot
import webbrowser

from list_columns_header import load_template_header, sample_column_header

myDict={}
repeatable =[]
hardcoded = []
property = ''
repeatative_value = ''




'''
@function : filepath_funct()
@brief    : this function used for getting pdf file path
@return   : it will give filepath of pdf file in system directory 
'''

def filepath_funct():
    try:
        root = tk.Tk()
        filepath = filedialog.askopenfilename()
        print(filepath)
        root.destroy()
        return filepath
    except:
        print("Error in Execution")
    
        

'''
@function : table_extract()
@brief    : this function used to extract table from the pdf file
@param    : filepath = filedialog.askopenfilename()
@return   : this function import all table from pdf file and export into xlsx file format
'''

def table_extract(filepath):
    try:
        table = camelot.read_pdf(filepath,pages='all')
        table.export('sample_data.xlsx',f = 'excel')
        return 0
    except:
        print("Error in Execution")

'''
@function : myDatabase():
@brief    : this function gives dictionary from two list of columns header.
'''

def myDatabase(list1,list2):
    try:
        for i in list2:
            print('Select the value for->',i,'\nfrom below list using numbers, \nin case does not fond option in \nbelow list select 100 to give input',list1)
            value=int(input('-->: '))
    
            if value==100:
                hardcoded.append(i)
                property=input('select the property->: ')
                                    
            else:
                property= list1[value-1]
                myDict[i]=property
        
            repeatative_value=input('Enter y to add this reapeated or n to remove from reapeatable-->: ')
            if repeatative_value == 'y':
                repeatable.append(i)
    except:
        print('error occur')
    
    