from tkinter import *
root=Tk()
root.title("Using Listbox")
label=Label(root,text="Select Language").pack(padx=10,pady=10)
list=Listbox(root,selectmode='mutliple')
list.pack(padx=10,pady=10)
x=['c','python','HTML','Ruby','JAVA','Oracle']
for item in range(len(x)):
    list.insert(END,x[item])
root.mainloop()    
