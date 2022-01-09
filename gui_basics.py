from tkinter import *
from tkinter import messagebox

window= Tk()
window.geometry("500x500")
window.configure(bg="Black")

cb1=IntVar()
cb2=IntVar()
cb3=IntVar()
cb4=IntVar()
cb5=IntVar()
cb6=IntVar()

def fun():
    msg="You Have Selected \n"
    if(cb1.get()==1):
        msg=msg+"Chocolate\n"
    if(cb2.get()==1):
        msg=msg+"Strawberry\n"
    if(cb3.get()==1):
        msg=msg+"Mango\n"
    if(cb4.get()==1):
        msg=msg+"Python\n"
    if(cb5.get()==1):
        msg=msg+"Java\n"
    if(cb6.get()==1):
        msg=msg+"C++\n"
    messagebox.showinfo("Welcome",msg)

frame=LabelFrame(window,text="Login",padx=50,pady=50)
frame.pack(padx=50,pady=50)


l1=Label(frame,text="Select Programming Language")
l1.pack()

c4=Checkbutton(frame,text="Python",variable=cb4,onvalue=1,offvalue=0)
c4.pack()
c5=Checkbutton(frame,text="Java",variable=cb5,onvalue=1,offvalue=0)
c5.pack()
c6=Checkbutton(frame,text="C++",variable=cb6,onvalue=1,offvalue=0)
c6.pack()

l1=Label(frame,text="Select Your Flavour")
l1.pack()

c1=Checkbutton(frame,text="Chocolate",variable=cb1,onvalue=1,offvalue=0)
c1.pack()
c2=Checkbutton(frame,text="Strawberry",variable=cb2,onvalue=1,offvalue=0)
c2.pack()
c3=Checkbutton(frame,text="Mango",variable=cb3,onvalue=1,offvalue=0)
c3.pack()
b1=Button(frame,text="Submit",command=fun)
b1.pack()
