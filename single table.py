Create a new table
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KU0CRG6\SQLEXPRESS;'
                      'Database=a;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('create table Books (Id INT PRIMARY KEY IDENTITY(1,1),
      Name VARCHAR (50) NOT NULL,
      Price INT)')
conn.commit()
conn.close()


import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KU0CRG6\SQLEXPRESS;'
                      'Database=a;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
record_1= ["Book - B", 300]
record_2= ["Book - C", 200]      
   
record_list = []
record_list.append(record_1)
record_list.append(record_2)
    
insert_records = 'INSERT INTO Books(Name, Price) VALUES(?,?) ' 
cursor.executemany(insert_records, record_list)
cursor.execute('select * from Books')
for row in cursor:
    print(row)
conn.commit()
conn.close()

#Output will be seen in the interactive mode.
###################################
Update a record 

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KU0CRG6\SQLEXPRESS;'
                      'Database=a;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
update_query = 'UPDATE Books SET Price = 500 WHERE Id= 2'
cursor.execute(update_query)
cursor.execute('select * from Books')
for row in cursor:
    print(row)
conn.commit()
conn.close()

