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

# buttons
button_viewall=Button(window,text="View All",width=15)
button_viewall.grid(row=2,column=3)
button_searchentry=Button(window,text="Search Entry",width=15)
button_searchentry.grid(row=3,column=3)
button_addentry=Button(window,text="Add Entry",width=15)
button_addentry.grid(row=4,column=3)
button_updateselected=Button(window,text="Update Selected",width=15)
button_updateselected.grid(row=5,column=3)
button_deleteselected=Button(window,text="Delete Selected",width=15)
button_deleteselected.grid(row=6,column=3)
button_close=Button(window,text="Close",width=15)
button_close.grid(row=7,column=3)

# end program and close window
window.mainloop()
