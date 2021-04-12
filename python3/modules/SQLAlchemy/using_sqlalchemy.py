#!/usr/bin/python3


import os
import sys

# An itemized list of imports to demonstrate what is needed for basic use of this ORM
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename = 'address'
    # Same as above. Define columns for 'address' table
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


# NEXT
# Create an engine that stores data in the local directory's sqlalchemy_example.db file
engine = create_engine('example.db')


# Create all tables in the engine. This is equivalent to "create table" statements in raw SQL
Base.metadata.create_all(engine)

# With the above code a database called 'example.db' will be generated in the current directory.


