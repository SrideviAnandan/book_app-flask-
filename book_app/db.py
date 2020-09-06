import sqlite3

conn = sqlite3.connect('book.sqlite')

cursor = conn.cursor()
sql_query = """ CREATE TABLE readers_writers(
             id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
             book_id int,
             author_id int,
             FOREIGN KEY (book_id) REFERENCES readers(id)
             FOREIGN KEY (author_id) REFERENCES writers(id)
             ALTER TABLE table_name
             ADD name text;
            )"""      
sql_query1 = """ CREATE TABLE readers(
             id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
             genre text NOT NULL,
             publisher text NOT NULL,
             name  text NOT NULL,
             price float NOT NULL
            )"""
sql_query2 = """ CREATE TABLE writers(
             id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
             name text NOT NULL
            )"""

cursor.execute(sql_query)
cursor.execute(sql_query2)
cursor.execute(sql_query1)