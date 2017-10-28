import sqlite3
# import everything from tkinter
from tkinter import *

# create empty window
window=Tk()

###################################################

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

def view():
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    # store the elements in our table as a list
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(item,quantity,price):
    conn=sqlite3.connect("app-5/lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def delete(item):
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close

def update(item,quantity,price):
    conn=sqlite3.connect("classes/15-Databases/lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close

#print(view())
############################################################

# create a new button
#b1=Button(window,text="Convert",command=km_to_miles)
#b1.grid(row=2,column=4)

# title input area
label_title=Label(window,text="Title: ")
label_title.grid(row=0,column=0)
entry_title_var=StringVar()
entry_title=Entry(window,textvariable=entry_title_var)
entry_title.grid(row=0,column=1)

# author input area
label_author=Label(window,text="Author: ")
label_author.grid(row=0,column=2)
entry_author_var=StringVar()
entry_author=Entry(window,textvariable=entry_author_var)
entry_author.grid(row=0,column=3)

# year input area
label_year=Label(window,text="Year: ")
label_year.grid(row=1,column=0)
entry_year_var=StringVar()
entry_year=Entry(window,textvariable=entry_year_var)
entry_year.grid(row=1,column=1)

# isbn input area
label_isbn=Label(window,text="ISBN: ")
label_isbn.grid(row=1,column=2)
entry_isbn_var=StringVar()
entry_isbn=Entry(window,textvariable=entry_isbn_var)
entry_isbn.grid(row=1,column=3)

# end program and close window
window.mainloop()
