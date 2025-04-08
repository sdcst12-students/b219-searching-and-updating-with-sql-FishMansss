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
    os.system('cls')
    if c==1:
        os.system('cls')
        print("First Name:")
        fn = str(input())
        print("Last Name:")
        ln = str(input())    
        print("Email:")
        em = str(input())
        print("Address:")
        ad = str(input())
        print("City:")
        ci = str(input())
        print("Postal Code:")
        pc = str(input())    

        cursor.execute(f"INSERT INTO record(fname, lname, email, address, city, pcode) values('{fn}','{ln}','{em}','{ad}','{ci}','{pc}');")
    if c==2:
        sel = input("Select a record by id: ")
        cha = input("Select element (fname = firstname, lname = lastname, email = email, ad = address, ci = city, pcode = postalcode ): ")
        new = input("New value: ")
        cursor.execute(f"UPDATE record SET '{cha}'= '{new}' WHERE id='{sel}';")
    if c==3:
        cursor.execute(f'SELECT * from record;')
        result = cursor.fetchall()
        for i in result:
            print(f"ID: {i[0]}")
            print(f"First Name: {i[1]}")
            print(f"Last Name: {i[2]}")
            print(f"Email: {i[3]}")
            print(f"Address: {i[4]}")
            print(f"City: {i[5]}")
            print(f"Postal Code: {i[6]}")
            print("")
        input()

    if c==4:
        connection.commit()
        exit()
    if c==5:
        cursor.execute("DROP TABLE record")
        cursor.execute("create table if not exists record(id integer primary key autoincrement, fname tinytext, lname tinytext, email tinytext, address tinytext, city tinytext, pcode tinytext);")

