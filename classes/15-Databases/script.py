import sqlite3

def create_table():
    # create connection
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    # create cursor object
    cur=conn.cursor()
    # execute sql command
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit changes to the db
    conn.commit()
    # close connection
    conn.close()

def insert(item,quantity,price):
    # create connection
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    # create cursor object
    cur=conn.cursor()
    # execute sql command
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    # commit changes to the db
    conn.commit()
    # close connection
    conn.close()

insert("Coffe Cup",23,7)
