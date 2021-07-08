#!/usr/bin/python3



import pymysql

user_id = input("Enter username: ")
password = input("Enter password: ")
db = pymysql.connect("localhost", user_id, password, "testdb")


cursor = db.cursor()


cursor.execute("show tables;")









