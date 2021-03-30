#!/usr/bin/python3

import texttable



# CREATE TABLE OBJECT
# ---------------------------------------------------------------------------

# Creating table object from Texttable class
table_object = texttable.Texttable(0)
# max_width must be an integer,whose value is maximum width of the table
# if set to 0, size is unlimited (self adjustible according to text inside cell),
# therefore cells won't be wrapped so it's recommended to use 0


# CREATE AND SET COLUMN ALIGNMENT
# ---------------------------------------------------------------------------

# This method creates the columns
# Each argument to this method creates a column and the letters 'l', 'r', 'c' set the column alignment
table_object.set_cols_align(["l", "l", "r", "c"])
# Set the desired columns alignment:
# "l" refers to column flushed left
# "c" refers to  column centered
# "r" refers to column flushed right


# SET COLUMN DATA-TYPES [OPTIONAL]
# ---------------------------------------------------------------------------

# Set datatype for each of the columns - [This step is optional]
table_object.set_cols_dtype(["t", "i", "f", "a"])
# texttable objects supports five types of data types:
# "t" refers to text
# "f" refers to decimal
# "e" refers to exponent
# "i" refers to integer
# "a" refers to automatic


# SET COLUMN VERTICAL ALIGNMENT
# ----------------------------------------------------------------------------

table_object.set_cols_valign(["t", "t", "m", "b"])
# Set the desired columns vertical alignment the elements of the 
# array should be either "t", "m" or "b":
# "t" refers to column aligned on the top of the cell
# "m" refers to column aligned on the middle of the cell
# "b" refers to column aligned on the bottom of the cell 


# ADDING ROW TO THE TABLE
# ----------------------------------------------------------------------------

table_object.add_rows([
    ["Text Header", "Integers", "Floats", "Auto column"],
    ["my dog skip", (17 + 11), 41.373, "Chrysanthamum"],
    ["This is a very long text line", 14, 48.23, "word"],
    ["line", 3, 1.2, "Hello"],
])
# add_rows(self, rows, header=True):
# The 'rows' argument can be either an iterator returning arrays, or a
# by-dimensional array.
# 'header' specifies if the first row should be used as the header of the table



# DRAW THE TABLE OBJECT TO STDOUT
# ----------------------------------------------------------------------------
print(table_object.draw())



# OUTPUT

#+-------------------------------+----------+--------+---------------+
#|          Text Header          | Integers | Floats |  Auto column  |
#+===============================+==========+========+===============+
#| my dog skip                   | 28       | 41.373 | Chrysanthamum |
#+-------------------------------+----------+--------+---------------+
#| This is a very long text line | 14       | 48.230 |     word      |
#+-------------------------------+----------+--------+---------------+
#| line                          | 3        |  1.200 |     Hello     |
#+-------------------------------+----------+--------+---------------+





