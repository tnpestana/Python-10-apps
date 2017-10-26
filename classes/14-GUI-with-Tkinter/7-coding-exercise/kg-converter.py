# import everything from tkinter
from tkinter import *

# create empty window
window=Tk()

def kg_converter():
    # store input value as float
    kg=float(e1_value.get())
    # convert to grams and insert
    grams=kg*1000
    t_grams.insert(END,grams)
    # convert to pounds
    pounds=kg*2.20462
    t_pounds.insert(END,pounds)
    # convert to ounces
    ounces=kg*35.274
    t_ounces.insert(END,ounces)

# create a new label widget
l1=Label(window,text="Kg")
l1.grid(row=0,column=0)

# create a variable to hold the input data
e1_value=StringVar()
# create a new input area widget
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

# create a new button
b1=Button(window,text="Convert",command=kg_converter)
# postiion the created button
b1.grid(row=0,column=2)

# create grams text widget
t_grams=Text(window,height=1,width=20)
t_grams.grid(row=1,column=0)

# create pounds text widget
t_pounds=Text(window,height=1,width=20)
t_pounds.grid(row=1,column=1)

# create ounces text widget
t_ounces=Text(window,height=1,width=20)
t_ounces.grid(row=1,column=2)

# end program and close window
window.mainloop()
