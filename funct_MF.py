'''
@File  : funct_MF.py
@brief : this file contain varios function which will be used
'''

import tkinter as tk
from tkinter import filedialog
import camelot

'''
@function : filepath_funct()
@brief    : this function used for getting file path
'''

def filepath_funct():
    filepath = filedialog.askopenfilename()
    print(filepath)
    return filepath




