from tkinter import *
root=Tk()
root.geometry('200x150')
frame=Frame(root).pack()
my_entry1=Entry(frame,width=20)
my_entry1.insert(0,'Username')
my_entry1.pack(padx=5,pady=5)
my_entry2=Entry(frame,width=20)
my_entry2.insert(0,'Password')#index,string
my_entry2.pack(padx=5,pady=5)
root.mainloop()