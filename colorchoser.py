from tkinter import colorchooser
from tkinter import *
root=Tk()

def choose_color():
    color_code=colorchooser.askcolor(title="choose color")
    print(color_code)
    

color=Button(root,text='select color',command=choose_color)
color.pack()
root.geometry('300x200')
root.mainloop()