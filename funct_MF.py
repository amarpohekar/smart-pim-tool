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
# filepath=''
myDict={}
repeatable=[]
property=''
repeatative_value=''
# list1=[]
# list2=[]



'''
@function : filepath_funct()
@brief    : this function used for getting pdf file path
@return   : it will give filepath of pdf file in system directory 
'''

def filepath_funct():
    filepath = filedialog.askopenfilename()
    print(filepath)
    return filepath


'''
@function : table_extract()
@brief    : this function used to extract table from the pdf file
@param    : filepath = filedialog.askopenfilename()
@return   : this function import all table from pdf file and export into xlsx file format
'''

def table_extract(filepath):
    table = camelot.read_pdf(filepath,pages='all')
    table.export('sample_data.xlsx',f = 'excel')
    return 0
    

'''
@function : myDatabase():
@brief    : this function gives dictionary from two list of columns header.
'''

def myDatabase(list1,list2):
    for i in list2:
        print('select the value from below list',i,'\nby using number system,\n if in case does not find in list then gives 100 as input',list1)
        value=int(input(''))
        
        if value==100:
            property=print('Select the Specific value->: ')
            
        else:
            property= list1[value-1]
            myDict[i]=property
            
        repeatative_value=input('if value is repeatative print y or n for discard the value from reapeatable->: ')
        if repeatative_value == y:
            repeatable.append(i)
        
        print('myDict-->',myDict)
        print('reapatable->',repeatable)
        


