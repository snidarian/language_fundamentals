#!/usr/bin/python3


import os
import sys

# An itemized list of imports to demonstrate what is needed for basic use of this ORM

# to make section 1 work
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# to make section 2 work
from sqlalchemy.orm import sessionmaker
# You can import table classes from other programs to work in the current program

# section 1

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Same as above. Define columns for 'address' table
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


# NEXT
# Create an engine that stores data in the local directory's sqlalchemy_example.db file
engine = create_engine('sqlite:///example.db')


# Create all tables in the engine. This is equivalent to "create table" statements in raw SQL
Base.metadata.create_all(engine)

# With the above code a database called 'example.db' will be generated in the current directory.


# section 2 - adding values to the tables

# engine = create_engine('sqlite:///example.db')

# bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()



session = DBSession()
 
# Insert a Person in the person table
new_person = Person(name='new person')
session.add(new_person)
session.commit()
 
# Insert an Address in the address table
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()




# finds person objects in Person table and returns their memory locations
#print(session.query(Person).all())


# return first person object in database
person = session.query(Person).first()
print(person.name)



# Find all addresses whose person field is pointing to the person object
session.query(Address).filter(Address.person == person).all()


# Retrieve one Address whose person field is point to the person object
session.query(Address).filter(Address.person == person).one()



address = session.query(Address).filter(Address.person == person).one()
address.post_code














