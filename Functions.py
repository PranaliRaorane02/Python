#Hello funtion
def display():
    print("Hello")

display()

#Parameters/Arguments
#1.Sum
def add(a,b):
    c=a+b
    print("The Addition Is",c)
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
add(a,b)
    

#2.Greater Number
def num(a1,b1):
    if(a1>b1):
        print(a1,"is greater")
    else:
        print(b1,"is greater")
a1=int(input("Enter First Number:"))
b1=int(input("Enter Second Number:"))
num(a1,b1)

#Range and Print
def display():
    n=int(input("Enter Range:"))
    for i in range(1,n+1):
        print(i)
display()


#Print List with Element Range
def list1(n1):
    p=[]
    for i in range(n1):
        m=input("Enter The Element:")
        p.append(m)
    print(p)
n1=int(input("Enter Number Of Elements:"))
list1(n1)

#Greatest Function
def greatest(e,f,g):
    max=e
    if(f>max):
        max=f
    if(g>max):
        max=g
    return max
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))
o=greatest(x,y,z)
print("The Greatest Number Is:",o)

#Lambda/Anonymous
list13=[12,23,45,88,99]
print("Given List:",list13)
evenlist= list(filter(lambda x: (x%2==0), list13))
print("Even elements are:",evenlist)
            
