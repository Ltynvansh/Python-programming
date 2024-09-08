from tkinter import *
root=Tk()
root.title("Using checkbutton")
def display():
    print("mall",checkbutton1)
var1=IntVar()
var2=IntVar()
checkbutton1=Checkbutton(root,text='mall',variable=var1,command=display).pack()
checkbutton2=Checkbutton(root,text='hello',variable=var2).pack()
root.mainloop()