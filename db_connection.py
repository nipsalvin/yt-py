import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user="root", passwd="", database = "nips")

mycursor = mydb.cursor()

mycursor.execute("select * from students")

for i in mycursor:
    print (i)