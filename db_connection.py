#Make sure you have mysql installed
#Make sure MySql service is running
import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user="root", passwd="", database = "nips") #Specify database and credentials here

mycursor = mydb.cursor()

mycursor.execute("select * from students") #enter mysql query here

for i in mycursor:
    print (i)