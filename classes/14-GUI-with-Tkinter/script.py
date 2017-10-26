# import everything from tkinter
from tkinter import *

# create empty window
window=Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

# create a new button
b1=Button(window,text="Convert",command=km_to_miles)
# postiion the created button
b1.grid(row=0,column=0)

# create a new input area
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

# create a new text widget
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

# end program and close window
window.mainloop()
