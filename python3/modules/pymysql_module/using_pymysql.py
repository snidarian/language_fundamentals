#!/usr/bin/python3



import pymysql
from getpass import getpass


password = getpass(prompt="MySQL pass for root: ")
db = pymysql.connect("localhost", "root", password, "testdb")

cursor = db.cursor()


result = cursor.execute("show tables;")

print(result)




