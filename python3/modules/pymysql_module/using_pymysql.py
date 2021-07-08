#!/usr/bin/python3



import pymysql
from getpass import getpass


password = getpass(prompt="MySQL root password: ")
db = pymysql.connect("localhost", "root", password, "testdb")

cursor = db.cursor()


cursor.execute("SELECT VERSION();")


data = cursor.fetchone()
print("Database Version : %s " % data)







