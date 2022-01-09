from tkinter import *
from tkinter import messagebox

window= Tk()
window.geometry("750x750")
window.title("Restaurant Menu")
window.configure(bg="Black")

#Veg
cb1=IntVar()
cb2=IntVar()
cb3=IntVar()
cb4=IntVar()
cb5=IntVar()
cb6=IntVar()

#Non-Veg
cb7=IntVar()
cb8=IntVar()
cb9=IntVar()
cb10=IntVar()
cb11=IntVar()
cb12=IntVar()

#Image Options
bg1=PhotoImage(file="pizza.png")
bg2=PhotoImage(file="burger.png")
bg3=PhotoImage(file="pasta.png")
bg4=PhotoImage(file="cake.png")

#Main Function
def fun():
    cost=0
    msg="You Have Selected \n"
    if(cb1.get()==1):
        msg=msg+"Farmhouse Pizza\n"
        cost=cost+12
    if(cb2.get()==1):
        msg=msg+"Veggie Burger\n"
        cost=cost+14
    if(cb3.get()==1):
        msg=msg+"Mushroom Alfredo Pasta\n"
        cost=cost+15
    if(cb4.get()==1):
        msg=msg+"Veggie Sub Sandwich\n"
        cost=cost+13
    if(cb5.get()==1):
        msg=msg+"Veg Hakka Noodles\n"
        cost=cost+15
    if(cb6.get()==1):
        msg=msg+"Fudge Cake\n"
        cost=cost+11
    #Non-Veg
    if(cb7.get()==1):
        msg=msg+"BBQ Chicken Pizza\n"
        cost=cost+25
    if(cb8.get()==1):
        msg=msg+"Fried Chicken Burger\n"
        cost=cost+24
    if(cb9.get()==1):
        msg=msg+"Seafood Pasta\n"
        cost=cost+30
    if(cb10.get()==1):
        msg=msg+"Salami Sandwich\n"
        cost=cost+20
    if(cb11.get()==1):
        msg=msg+"Egg Hakka Noodles\n"
        cost=cost+23
    if(cb12.get()==1):
        msg=msg+"Fudge Cake\n"
        cost=cost+20
    
    messagebox.showinfo("Order","View Order")
    messagebox.showinfo("Your Order",msg)
    
    messagebox.showinfo("Payment","Make Payment")
    messagebox.showinfo("Pay $",cost)

#Order Function
def fun1():
    messagebox.showinfo("Confirm","Click Okay To Place Order")
    messagebox.showinfo("ORDER PLACED","Please Proceed To Payment")
    
    
frame=LabelFrame(window,text="Veg Menu",bg="beige")
frame.place(x=300,y=40,width=350,height=330)


l1=Label(frame,text="\n* * * * * * * * * * Select Your Order* * * * * * * * * * \n",bg="beige")
l1.pack()

#Veg Menu Options
c1=Checkbutton(frame,text="Farmhouse Pizza...............$12\n",variable=cb1,onvalue=1,offvalue=0,bg="beige")
c1.pack()
c2=Checkbutton(frame,text="Aloo Tikki Burger...............$14\n",variable=cb2,onvalue=1,offvalue=0,bg="beige")
c2.pack()
c3=Checkbutton(frame,text="Mushroom Alfredo Pasta...............$15\n",variable=cb3,onvalue=1,offvalue=0,bg="beige")
c3.pack()
c4=Checkbutton(frame,text="Veggie Sub Sandwich...............$13\n",variable=cb4,onvalue=1,offvalue=0,bg="beige")
c4.pack()
c5=Checkbutton(frame,text="Veg Hakka Noodles...............$15\n",variable=cb5,onvalue=1,offvalue=0,bg="beige")
c5.pack()
c6=Checkbutton(frame,text="Fudge Cake...............$11\n",variable=cb6,onvalue=1,offvalue=0,bg="beige")
c6.pack()

frame=LabelFrame(window,text="Non-Veg Menu",bg="beige")
frame.place(x=650,y=40,width=300,height=330)


l3=Label(frame,text="\n* * * * * * * * * * Select Your Order* * * * * * * * * * \n",bg="beige")
l3.pack()

#Non-Veg Menu Options
c7=Checkbutton(frame,text="BBQ Chicken Pizza...............$25\n",variable=cb7,onvalue=1,offvalue=0,bg="beige")
c7.pack()
c8=Checkbutton(frame,text="Fried Chicken Burger...............$24\n",variable=cb8,onvalue=1,offvalue=0,bg="beige")
c8.pack()
c9=Checkbutton(frame,text="Seafood Pasta...............$30\n",variable=cb9,onvalue=1,offvalue=0,bg="beige")
c9.pack()
c10=Checkbutton(frame,text="Salami Sandwich...............$20\n",variable=cb10,onvalue=1,offvalue=0,bg="beige")
c10.pack()
c11=Checkbutton(frame,text="Egg Hakka Noodles...............$23\n",variable=cb11,onvalue=1,offvalue=0,bg="beige")
c11.pack()
c12=Checkbutton(frame,text="Fudge Cake...............$20\n",variable=cb12,onvalue=1,offvalue=0,bg="beige")
c12.pack()


#Adding Images
l2=Label(window,image=bg4)
l2.place(x=0,y=400,width=500,height=300)
l4=Label(window,image=bg3)
l4.place(x=860,y=400,width=400,height=300)


#Order Buttons
b1=Button(window,text="Place Order",command=fun1,bg="beige")
b1.place(x=595,y=500,width=150,height=55)
b2=Button(window,text="Order Summary And Payment",command=fun,bg="beige")
b2.place(x=550,y=570,width=250,height=55)


