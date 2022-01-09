from tkinter import *

root=Tk()
root.geometry('640x900')

scvalue=StringVar()
scvalue.set('')
screen = Entry(root,textvar=scvalue,font='lucida 40 bold')
screen.pack(fill=X,ipadx=8,pady=10,padx=10)