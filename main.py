# import neccessarylibraries
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "stop! Virus found.")

button=Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()