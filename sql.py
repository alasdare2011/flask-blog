#sql.py - Create a SQLite3 table and populate it with data

import sqlite3

#create new database if the database does not exist
with sqlite3.connect("blog.db") as connection:

    #get cursor object used to execute SQL commands
    c = connection.cursor()

    #create table
    c.execute("""CREATE TABLE posts
                (title TEXT, post TEXT)
                """)

    #insert dummy text into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')