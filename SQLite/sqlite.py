"""
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and
allows accessing the database using a nonstandard variant of the SQL query language.

"""

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")
conn.close()
