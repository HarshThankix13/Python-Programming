#pip Install pymysql

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

mycursor = mydb.cursor()

#create database in mysql
mycursor.execute("Create Database If Not Exists 15Jun_Crud")
mydb.commit() #save and execute 

mydb = pymysql.connect(host="localhost",user="root",password="",database="15Jun_Crud")
mycursor = mydb.cursor()
#Create Table Inside The Database 

mycursor.execute("Create Table  If Not Exists Student (id int primary key auto_increment , name varchar(20) , subject varchar(20), city varchar(20) )")
mydb.commit()
