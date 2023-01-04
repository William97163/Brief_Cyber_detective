import pandas as pd
import sqlite3

connection = sqlite3.connect('books.db')

cursor = connection.cursor()

cursor.execute(
    'Create table IF NOT EXISTS book (id INT,title VARCHAR(255),stars INT,prices FLOAT,instock varchar(255))')
