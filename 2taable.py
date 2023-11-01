import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KU0CRG6\SQLEXPRESS;'
                      'Database=hospital;'
                      'Trusted_Connection=yes;')
cur = conn.cursor()

#The above statements are common for all sections
#sections are separated by the # lines
###########################
cur.execute(''' create table doctor (Id INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR (50) NOT NULL,	                                                              Specialised VARCHAR(50) NOT NULL)  ''')
conn.commit()
conn.close()
##########################
#to create a table patient which has a FK DoctorId and refers to the PK Id in doctor table.
cur.execute('''  create table patient ( Id INT PRIMARY KEY IDENTITY(1,1),
                                                              Name VARCHAR (50) NOT NULL,
                                                              DoctorId INT foreign key references doctor(Id))  ''')
conn.commit()
conn.close()                                 
##############################
#to insert data rows into doctor table
cur.execute(''' insert into doctor (Name,Specialised) values ('KrishnaKumar','Gynaecology'),
                                                                                                         ('Bhattacharya','General Physician')  ''')
cur.execute('select * from doctor')
for row in cur:
     print(row)
conn.commit()
conn.close()
###########################
#to insert rows into patient table
cur.execute(''' insert into patient (Name,DoctorId) values ('Rajneet',1),
                                                                                                ('Sameer',2)  ''')
cur.execute('select * from patient')
for row in cur:
       print(row)
conn.commit()
conn.close()

############################
#to update rows in doctor table
cur.execute(''' update doctor SET Specialised = 'Ortho' WHERE Id= 2  ''')
cur.execute('select * from doctor')
for row in cur:
    print(row)
conn.commit()
conn.close()

############################
#to update rows in patient table
cur.execute(''' update patient SET DoctorId = 1 WHERE Id= 2  ''')
cur.execute('select * from patient')

for row in cur:
       print(row)
conn.commit()
conn.close()

############################
#delete rows from patient table
cur.execute('''  delete from patient  WHERE Id= 1  ''')
cur.execute('select * from patient')
for row in cur:
    print(row)
conn.commit()
conn.close()

#########################


cur.execute(''' insert into patient (Name,DoctorId) values ('Ratna',2),
                                                                                                ('Sonu',2)  ''')
cur.execute('select * from patient')

for row in cur:
       print(row)
conn.commit()
conn.close()

##########################
#delete rows from patient table

cur.execute('''  delete from patient  WHERE Id= 2  ''')
cur.execute('select * from patient')

for row in cur:
    print(row)
conn.commit()
conn.close()

########################
#delete rows from doctor table

cur.execute('''  delete from doctor  WHERE Id= 1  ''')
cur.execute('select * from doctor')
##
for row in cur:
    print(row)
conn.commit()
conn.close()

