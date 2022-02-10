'''
@file  : main.py
@brief : this application file 

'''



import Machflex_logic
import list_columns_header

filepath = ''
list1=[]
list2=[]



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
                               4> Create application data
                               5> Create final output
                               6> Exit
                               :-  '''))
        
        if option == 1:
            
            filepath = Machflex_logic.filepath_funct()
        
        elif option == 2:
            Machflex_logic.table_extract(filepath)
            
        elif option == 3:
            filepath = Machflex_logic.filepath_funct()
            
        elif option == 4:
            list1 = list_columns_header.sample_column_header()
            list2 = list_columns_header.load_template_header()
            Machflex_logic.myDatabase(list1,list2)
            print('database created below-> ',Machflex_logic.myDict)
            print('Repeatable list created-> ',Machflex_logic.repeatable)
                    
        else:
            exit()       
                
            