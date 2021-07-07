#!/usr/bin/python3



import pymysql


db = pymysql.connect("localhost", "testuser", "test123", "testdb")


cursor = db.cursor()


cursor.execute("show tables;")









