from tkinter import *


root = Tk()
root.title("MyApp")

myvar = StringVar()

def myvarWritten(*args):
    print("myvarWritten",myvar.get())

myvar.trace("w", myvarWritten)

text_entry = Entry(root, textvariable=myvar)
text_entry.pack()

root.mainloop()