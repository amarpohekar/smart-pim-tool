'''
@file  : main.py
@brief : this application file 

'''




import funct_MF
import list_columns_header


filepath = ''
list1=[]
list2=[]
myDict={}
repeatable=[]
repeatative_value=''
property= ''


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
                               4> print all columns header in list from load tempplate file
                               5> Print all column header in list fron Sample data
                               6> create the Dictionnary and repeatable list by using refferance of lists of columns header of load template and sample data 
                               7> Exit
                               :-  '''))
        
        if option == 1:
            filepath = funct_MF.filepath_funct()
        
        elif option == 2:
            funct_MF.table_extract(filepath)
            
        elif option == 3:
            filepath = funct_MF.filepath_funct()
            
        elif option == 4:
            list_columns_header.load_template_header()
        
        elif option == 5:
            list_columns_header.sample_column_header()
        
        elif option == 6:
            list1 = list_columns_header.sample_column_header()
            list2 = list_columns_header.load_template_header()
            funct_MF.myDatabase()
            
                    
        else:
            exit()       
                
            