#! /usr/bin/python3

import sqlite3

# returns a connection object - this line creates the database if it does not already exist
connection = sqlite3.connect("aquarium.db")


# verify successully created db with this line
# connection.total_changes is the number of rows that have been changed by the connection object
# print(connection.total_changes)

cursor = connection.cursor()


# The cursor.execute object-method is used to interact with the database

# Creates table in the database
# cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")


# data is inserted into the tables in this format.
cursor.execute("INSERT INTO fish VALUES ('jamie', 'cuttlefish', 7)")
cursor.execute("INSERT INTO fish VALUES ('sammy', 'shark', 1)")



# cursor.execute([SQL statments}).fetchall() allows you to fetch all results of a SELECT statement



# reading data from the database
rows = cursor.execute("SELECT * FROM fish").fetchall()
# saving the output into a file 'rows' and then printing it.
print(rows)



# Using a WHERE clause in an sql query - example
# use '?' to bind arguments to your SQL statements instead of using python string operations
# Doing it this way protects you against SQL injection attacks
target_fish_name = "jamie"
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name = ?", (target_fish_name,),
    ).fetchall()
print(rows)





while True:
   fish_name = input("Add fish name to the database: ")
   fish_species = input("Fish species: ")
   fish_tank = input("Which tank is the fish in? (integer): ")
   cursor.execute("INSERT INTO fish VALUES (?, ?, ?)", (fish_name, fish_species, fish_tank))
   rows = cursor.execute("SELECT * FROM fish").fetchall()
   for row in rows:
       print(row, end='\n')
   break
   



# The following statements are necessary for saving results in the database.
# .commit method is absolutely necessary if you want the data modified to remain in persistent storage
connection.commit()


connection.close()










