import connection

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="",database="15Jun_Crud")
mycursor = mydb.cursor()

menu =  """

                    MENU 
            
            Press 1 For Add Student 
            Press 2 For View Students
            Press 3 For update Students
            Press 4 For delete Students
            Press 5 For select Students
            Press 6 For Exit
                    


"""

print(menu)
choice = int(input("Enter Your Choice : "))
if choice == 1 :
    #add data
    name = input("Enter Name : ")
    subject = input("Enter Subejct : ")
    city = input("Enter City : ")
    
    values = (name,subject,city)
    
    str = "insert into Student (name,subject,city) values('%s','%s','%s')"
    mycursor.execute(str % values)
    mydb.commit()
    print("Successfully Data Inserted ")
    

elif choice == 2:
    #view data
    query = "select * from Student "
    mycursor.execute(query)
    
    data = mycursor.fetchall()
    
    print(data)

elif choice == 3:
    name = input("Enter Your Name : ")
    updatedname = input("Enter Name : ")
    subject = input("Enter Subject : ")
    city = input("Enter City : ")
    
    values = (updatedname, subject , city , name)
    query = "update Student set name='%s' , subject = '%s' , city = '%s' , 'where name = '%s' "
    mycursor.execute(query % values)
    mydb.commit()
    
elif choice == 5:
    #fetch specific data from the table
    name = input("Enter Name : ")
    query = "Select * from Student Where Name = '%s'" 
    values = (name)
    mycursor.execute(query % values)
    data= mycursor.execute.fetchone()
    
    print("name = ",data[1])
    print("subject = ", data[2])   