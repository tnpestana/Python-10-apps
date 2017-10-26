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
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    # store the elements in our table as a list
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
