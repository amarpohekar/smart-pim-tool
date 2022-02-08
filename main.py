'''
@file  : main.py
@brief : this application file 
'''

import funct_MF



filepath = ''

if __name__=="__main__":
    print('''
          .
          .
          Welcome to the demo ''')
    while True == 1:
        option = int(input(''' Selct one of the following option
                               1> Select and open the load TDS
                               2> Select the pdf File
                               3> Extract the table from pdf file
                               4> Select load template file
                               5> Print all column header
                               6> Select the Sample load tempplate file
                               7> Exit
                               :-  '''))
        if option ==1:
            funct_MF.openload()
        
        elif option == 2:
            filepath = funct_MF.filepath_funct()
            print(filepath)
        
        elif option == 3:
            funct_MF.table_extract(filepath)
            
        elif option == 4:
            funct_MF.openload()
        
        elif option == 5:
            funct_MF.openload()
                            
        else:
            exit()       
                
            