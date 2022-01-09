from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Login Page")
window.geometry("800x550")
window.configure(bg="cornflower blue")

bg1=PhotoImage(file="icon.png")

l1= Label(window,text= "E-mail ID",bg="light steel blue")
l1.place(x=450,y=150,height=30,width=50)

l2=Label(window,text="Password",bg="light steel blue")
l2.place(x=450,y=210,height=30,width=55)

l3=Label(window,image=bg1)
l3.place(x=175,y=110,height=200,width=166)

e1=Entry(window,bd=5)# bd=border
e1.place(x=530,y=150)
e2=Entry(window,bd=5,show='*')
e2.place(x=530,y=210)

#Main Login
def login():
    a=str(e1.get())
    b=str(e2.get())
    if(a=='pranali@gmail.com' and b=='starwars'):
        messagebox.showinfo("Message","Login Successful")
    elif(a=='' or b==''):
        messagebox.showinfo("Message","E-mail ID or Password Cannot Be Blank")
    elif(a!='pranali@gmail.com' or b!='starwars'):
        messagebox.showinfo("Message","Incorrect E-mail ID or Password")
    
        

#Sign-Up
def click():
    window= Tk()
    window.title("Sign-up Page")
    window.geometry("800x400")
    window.configure(bg="misty rose")

    l4=Label(window,text="User Details",bg="beige")
    l4.place(x=350,y=10,height=30,width=100)

    l5=Label(window,text="Full Name",bg="beige")
    l5.place(x=250,y=80,height=30,width=65)

    l6=Label(window,text="Email-ID",bg="beige")
    l6.place(x=250,y=120,height=30,width=65)

    l7=Label(window,text="Date Of Birth",bg="beige")
    l7.place(x=250,y=160,height=30,width=80)

    l8=Label(window,text="Password",bg="beige")
    l8.place(x=250,y=200,height=30,width=65)

    e5=Entry(window,bd=5)
    e5.place(x=340,y=80)
    e6=Entry(window,bd=5)
    e6.place(x=340,y=120)
    e7=Entry(window,bd=5)
    e7.place(x=340,y=160)
    e8=Entry(window,bd=5,show='*')
    e8.place(x=340,y=200)

    
#Successful Sign-Up/Already Exists
    def sign():
        c=str(e6.get())
        d=str(e5.get())
        f=str(e7.get())
        g=str(e8.get())
        if(c=='pranali@gmail.com'):
            messagebox.showinfo("Message","This E-mail ID Already Exists")
        elif(c!= '' and d!= '' and f!='' and g!= ''):
            messagebox.showinfo("Message","Congratulations \nYou Are Signed-Up")
        else:
            messagebox.showinfo("Message","Please Fill All Details")

    b3=Button(window,text="Sign-Up",bg="beige",command=sign)
    b3.place(x=360,y=260,width=100,height=30)


l2=Label(window,text="Not Signed Up Yet?",bg="light steel blue")
l2.place(x=345,y=400,height=30,width=140)

b2=Button(window,text="Create Account",bg="light steel blue",command=click)
b2.place(x=367,y=450,width=100,height=30)

b1=Button(window,text="Enter",bg="light steel blue",command=login)
b1.place(x=550,y=275,width=70,height=30)







