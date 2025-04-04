import sqlite3
import os 
import time
os.system('cls')

##Establish table
file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor()

cursor.execute("create table if not exists record(id integer primary key autoincrement, fname tinytext, lname tinytext, email tinytext, address tinytext, city tinytext, pcode tinytext);")




##Choice to select opperation


    

##Selecting opperation

loop = True
while loop==True:
    print("             ||||||||||   record FILER   ||||||||||")
    print("\n\n")
    time.sleep(2)
    
    print("     >>1. Add a record")
    print("")
    print("     >>2. Edit a record")
    print("")
    print("     >>3. View record(s)")
    print("")
    print("     >>4. Save and Exit")
    print("")
    print("     >>5. Reset")
    c=int(input())
    
    if c==1:
        os.system('cls')
        print("First Name:")
        fn = input()
        print("Last Name:")
        ln = input()    
        print("Email:")
        em = input()
        print("Address:")
        ad = input()
        print("City:")
        ci = input()
        print("Postal Code:")
        pc = input()    

        cursor.execute(f"INSERT INTO record(fname, lname, email, address, city, pcode) values('{fn}','{ln}','{em}','{ad}','{ci}','{pc}');")
    if c==2:
        sel = input("Select a record by id:")
        cha = input("Select element")
        new = input("New value")
        cursor.execute(f'UPDATE record where id is "{sel}"("{cha}") values("{new}");')
        
    if c==3:
        cursor.execute(f'SELECT * in record;')
        result = cursor.fetchall()
        print(result)

    if c==4:
        exit()
    if c==5:
        cursor.execute("DROP TABLE record")
        cursor.execute("create table if not exists record(id integer primary key autoincrement, fname tinytext, lname tinytext, email tinytext, address tinytext, city tinytext, pcode tinytext);")

