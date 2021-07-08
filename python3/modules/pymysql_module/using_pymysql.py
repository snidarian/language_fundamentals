#!/usr/bin/python3



import pymysql


password = input("Enter password: ")
db = pymysql.connect("localhost", "root", password, "testdb")

cursor = db.cursor()


result = cursor.execute("select authentication_string from user;")

print(result)




