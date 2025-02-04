import psycopg2

def create_table():
    # create connection
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    # create cursor object
    cur=conn.cursor()
    # execute sql command
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit changes to the db
    conn.commit()
    # close connection
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    # store the elements in our table as a list
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close

def update(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close

create_table()
insert("Orange",10,2)
update("Orange",15,1)
#delete("Orange")
print(view())
