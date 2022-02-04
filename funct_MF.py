'''
@File  : funct_MF.py
@brief : this file contain varios function which will be used
'''

import tkinter as tk
from tkinter import filedialog
import camelot

'''
@function : filepath_funct()
@brief    : this function used for getting pdf file path
@return   : it will give filepath of pdf file insystem directory 
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
    table.export('sample_data.xlsx',f = 'xlsx')
    return 0
    

