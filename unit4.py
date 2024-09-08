from  tkinter import  *
root=Tk()
root.title("Using Canvas")
root.geometry("1287x685+50+50")#widthxheight+x+y
headingLabel=Label(root,text="My First Program")
headingLabel.pack()
root.configure(bg="yellow")#Background
#root.maxsize(200 ,300)#width,height
#root.minsize(20,30)
image=PhotoImage(file="C:\\Users\\hp\\Pictures\\Screenshots\\Screenshot (7).png")
img=Label(root,image=image).pack()
button=Button(root,text="Name").pack()

root.mainloop()