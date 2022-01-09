from tkinter import *

expression= ""

#Operations
def input_num(number,equation):
    global expression
    expression=expression+str(number)
    equation.set(expression)
def clear_input(equation):
    expression=" "
    expression.set("Enter The Expression")
def evaluate(equation):
    global expression
    try:
        result=str(eval(expression))
        equation.set(result)
        expression=" "
    except:
        expression=" "
        equation.set("Enter a Valid Expression")

#Calculator Design
window= Tk()
window.geometry("400x600")
window.configure(bg="black")
window.title("Calculator")
equation= StringVar()
e=Entry(window,bd=5,bg="misty rose",textvariable=equation)
e.place(x=0,y=0,width=400,height=150)
equation.set("Enter The Expression")



expression= ""

#Clear Expression
def input_num(number,equation):
    global expression
    expression=expression+str(number)
    equation.set(expression)
def clear_input(equation):
    global expression
    expression= ""
    equation.set("Enter The Expression")
def evaluate(equation):
    global expression
    try:
        result=str(eval(expression))
        equation.set(result)
        expression=" "
    except:
        expression=" "
        equation.set("Enter a Valid Expression")


#Buttons
b1=Button(window,text="7",bg="misty rose",command=lambda: input_num(7,equation))
b1.place(x=300,y=300,width=100,height=100)

b2=Button(window,text="8",bg="misty rose",command=lambda: input_num(8,equation))
b2.place(x=0,y=400,width=100,height=100)

b3=Button(window,text="9",bg="misty rose",command=lambda: input_num(9,equation))
b3.place(x=100,y=400,width=100,height=100)

b4=Button(window,text="4",bg="misty rose",command=lambda: input_num(4,equation))
b4.place(x=0,y=300,width=100,height=100)

b5=Button(window,text="5",bg="misty rose",command=lambda: input_num(5,equation))
b5.place(x=100,y=300,width=100,height=100)

b6=Button(window,text="6",bg="misty rose",command=lambda: input_num(6,equation))
b6.place(x=200,y=300,width=100,height=100)

b7=Button(window,text="1",bg="misty rose",command=lambda: input_num(1,equation))
b7.place(x=0,y=200,width=100,height=100)

b8=Button(window,text="2",bg="misty rose",command=lambda: input_num(2,equation))
b8.place(x=100,y=200,width=100,height=100)

b9=Button(window,text="3",bg="misty rose",command=lambda: input_num(3,equation))
b9.place(x=200,y=200,width=100,height=100)

bce=Button(window,text="CE",bg="misty rose",command=lambda: clear_input(equation))
bce.place(x=300,y=200,width=100,height=100)

b10=Button(window,text="0",bg="misty rose",command=lambda: input_num(0,equation))
b10.place(x=200,y=400,width=100,height=100)

b11=Button(window,text="+",bg="misty rose",command=lambda: input_num('+',equation))
b11.place(x=0,y=500,width=100,height=100)

b12=Button(window,text="-",bg="misty rose",command=lambda: input_num('-',equation))
b12.place(x=300,y=500,width=100,height=100)

b13=Button(window,text="x",bg="misty rose",command=lambda: input_num('*',equation))
b13.place(x=100,y=500,width=100,height=100)

b14=Button(window,text="/",bg="misty rose",command=lambda: input_num('/',equation))
b14.place(x=200,y=500,width=100,height=100)

b15=Button(window,text="=",bg="misty rose",command=lambda: evaluate(equation))
b15.place(x=300,y=400,width=100,height=100)
