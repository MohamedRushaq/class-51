# import neccessarylibraries
from tkinter import *

# setting up main window
root=Tk()
root.geometry("400x300")
root.title("main")

# function   to open new (Top Level) window
def topwin():
    # setting up  top window 
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    # adding  a lebel  widget to top window 
    l2=Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()

# Adding a lebel and button widget to root (main) window 
l=Label(root, text="This is root window")
btn=Button(root, text="Click here to open another window", command=topwin) 

# Arranging widgets
l.pack()
btn.pack()
root.mainloop()