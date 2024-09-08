#selection of numerical input
import tkinter as tk
def on_spinbox():
    value = spinbox.get()
    print("value is :",value)

root=tk.Tk()
root.geometry('300x200')
label=tk.Label(root,text='Spinbox').pack()
spinbox=tk.Spinbox(root,from_=0, to= 100,width=10,bg='yellow',fg='black',repeatinterval=100,command=on_spinbox)
spinbox.pack(padx=20,pady=20)
root.mainloop()

