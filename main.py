'''
@file  : main.py
@brief : this application file 
'''

import funct_MF
import list_columns_header


filepath = ''

if __name__=="__main__":
    print('''
          .
          .
          Welcome to the demo ''')
    while True == 1:
        option = int(input(''' Selct one of the following option
                               1> Select the pdf File
                               2> Extract the table from pdf file
                               3> Select load template file
                               4> print all columns header from load tempplate file
                               5> Print all column header Sample data
                               6> Exit
                               :-  '''))
        
        if option == 1:
            filepath = funct_MF.filepath_funct()
            print(filepath)
        
        elif option == 2:
            funct_MF.table_extract(filepath)
            
        elif option == 3:
            load_template = funct_MF.filepath_funct()
            print(load_template)
        
        elif option == 4:
            list_columns_header.load_template_header()
        
        elif option == 5:
            list_columns_header.sample_column_header
                
        else:
            exit()       
                
            