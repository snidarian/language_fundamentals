#!/usr/bin/python3

import sqlite3

# create connection to database
connection = sqlite3.connect('example.db')



# create cursor
c = connection.cursor()


# without an ORM you have to write thses sorts of SQL commands...

try:
    c.execute(
        '''
        CREATE TABLE person
        (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
        ''')
except:
    "Table 'person' already exists"        

try:
    c.execute(
        '''
        CREATE TABLE address
        (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
        post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL, FOREIGN KEY(person_id) REFERENCES person(id))
        ''')
except:
    "Table 'address' already exists"


c.execute(
    '''
    INSERT INTO person VALUES(1, 'pythoncentral')
    '''
)

c.execute(
    '''
    INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
    '''
)


# commit changes if there were any
connection.commit()


c.execute('SELECT * FROM person')
print(c.fetchall())
c.execute('SELECT * FROM address')
print(c.fetchall())


# closeout connection
connection.close()




















