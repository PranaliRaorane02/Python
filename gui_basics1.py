from tkinter import *
from tkinter import messagebox

window= Tk()
window.geometry("500x500")
window.configure(bg="Black")

rb=IntVar()

bg=PhotoImage(file="bf.png")

def fun():
    
    if(rb.get()==1):
        messagebox.showinfo("Welcome","Sci-Fi Selected")
    if(rb.get()==2):
        messagebox.showinfo("Welcome","Comedy Selected")
    if(rb.get()==3):
        messagebox.showinfo("Welcome","Drama Selected")

l2=Label(window,image=bg)
l2.place(x=0,y=0,relwidth=1,relheight=1)

l1=Label(window,text="Select Genre")
l1.pack()

r1=Radiobutton(window,text="Sci-Fi",variable=rb,value=1)
r1.pack()
r2=Radiobutton(window,text="Comedy",variable=rb,value=2)
r2.pack()
r3=Radiobutton(window,text="Drama",variable=rb,value=3)
r3.pack()

b1=Button(window,text="Submit",command=fun)
b1.pack()

