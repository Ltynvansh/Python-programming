import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("combobox")
ttk.Label(root,text='select month',font='Time New Roman').pack(anchor='w')
month=['jan','feb','mar','apr','may','june','july']
combobox1=ttk.Combobox(root,widtrh=10,heigth=10,value=month).pack(anchor='w')
root.mainloop()
