#!/usr/bin/python3
# tutorialspoint SQLAlchemy inspired SQLAlchemy doc-file



# engine class connects a pool and dialect together to provide source of database connectivity and behavior.

# an object of the engine class is instantiated using the 'create_engine()' function
# The create_engine() function takes a database as one argument 

from sqlalchemy import create_engine
# echo flag sets up SQLAlchemy logging. To hide verbose output set echo attribute to 'None'
engine = create_engine('sqlite:///college.db', echo = True)


# for a MySQL database use the below command -
#engine = create_engine("mysql://user:pwd@localhost/college", echo = True)


# to specifically mention DB-API to be used, the URL string will appear as follows
# dialect[+driver]://user:password@host/dbname

# example if you're using the PyMySQL driver with MySQL, use the following command..
# mysql+pymysql://<username>:<password>@<host>/<dbname>


# .connect() method returns database connection object
# connection_object = engine.connect()

# .execute() method executes a SQL statement construct (just like in SQLite3 module)


# ---------------------------------------------------------------------------------------
# Creating tables


# MetaData() class contains definitions of tables and associated objects
# Hence an object of MetaData class is a collection of Table objects and their associated schema constructs

from sqlalchemy import MetaData
# shorter alias for the class name
meta = MetaData()


# next we define our tables all within above metadata catalog, using the Table construct

# an object of Tabl class represents the corresponding table in a database.
# it takes the following parameters: Metadata (object that will hold this table), Column(s) (one or more objects of column class)



# let's create a students table in the college database...
from sqlalchemy import Table, Column, Integer, String, MetaData
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('lastname', String),
)


# the create_all() function uses the engine object to create all the defined table objects and stores the information in metadata.
meta.create_all(engine)



# --------------------------------------------------------------------------------
# SQL Expressions

# SQL expressions are constructed using methods on the target table object

# an insert object is create like so:
insert_object = students.insert()

# below statement shows you the raw SQL statement this method is creating
print(str(insert_object))


# in this way you can also use the .select(), .update(), and delete() methods

# ---------------------------------------------------------------------------------
# SQLAlchemy core - Executing expressions

#In order to execute the resulting SQL expressions, we have to obtain a connection object representing an actively checked out DBAPI connection resource
#and then feed the expression object as shown in the code below.
connection_object = engine.connect()


# create insertion object 
insertion_object = students.insert()


# You can use the values() method to insert values into the object (The statement is not yet executed)
insertion_object = students.insert().values(name = 'Jerdann', lastname = 'lanzig')

# Then you can execute the insertion object as an SQL statement by using the .execute method on
#  the connection_object with the insertion object as its single argument
# The below statement inserts and commmits the insertion object
connection_object.execute(insertion_object)



# to issue many insert using DBAPI's execute many() method, you can send in a list of dictionaries each 
# containing a distinct set of parameters to be inserted
# the below code uses an array of dictionary items as its insertion argument
connection_object.execute(students.insert(), [
    {'name': 'Philton', 'lastname' : 'Hammersmith'},
    {'name': 'Karl', 'lastname' : 'Riddenhambacher'},
    {'name': 'Smitty', 'lastname' : 'Jerbanmenjanson'},
    {'name': 'Ulric', 'lastname' : 'Smart'},
    {'name': 'Charlene', 'lastname' : 'bewbs'},
    {'name': 'Timmy', 'lastname' : 'Turner'},
    {'name': 'Rajan', 'lastname' : 'Swamiyaranarmani'},
    {'name': 'Pilcooth', 'lastname' : 'Rajals'},
    {'name': 'Duke', 'lastname' : 'Ellington'},
    {'name': 'Martin', 'lastname' : 'King'},
    {'name': 'Paul', 'lastname' : 'Syesta'},
])


# --------------------------------------------------------------------------------------------
# SQLAlchemy Core - SELECTING ROWS - SELECT statements


# the select() method of the table object allows us to construct a SELECT expression

selection_object = students.select()
# notice the result when we print this
print("selection_object appears as SELECT statement when printed:")
print(str(selection_object))


# You can use the selection_object as a parameter to .execute() method of connection_object
result = connection_object.execute(selection_object)


# We can fetch records using the fetchone() method
row = result.fetchone()

# This for loop prints all the results in the result variable
for row in result:
    print(row[0], row[2], row[1]) # this prints results in the order: (id, lastname, firstname)



# WHERE CLAUSE


selection_object = students.select().where(students.c.id>2) # here 'c' is an alias for column
# Then we execute that selection object as the parameter for .execute() method and set it to a variable
result = connection_object.execute(selection_object)

print("Results from SELECT statement with WHERE clause")
for row in result:
    print(row)



# --------------------------------------------------------------------------------------
# using the text() function - allows you to run RAW SQL statements 

from sqlalchemy import text

text_object = text("SELECT * FROM students")
result = connection_object.execute(text_object)

print("RAW SQL statements using text() function")
for row in result:
    print(row)


# The text()function requires Bound parameters in the named colon format. 
# They are consistent regardless of database backend. 
# To send values in for the parameters, we pass them into the execute() method as additional arguments.

selection_object = text("SELECT students.name, students.lastname FROM students WHERE students.name BETWEEN :x AND :y;")
print("Bind parameters SQL SELECT statement")
result = connection_object.execute(selection_object, x = 'A', y = 'G').fetchall()

for row in result:
    print(row)












