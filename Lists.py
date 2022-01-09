#Lists

#Operations
a=[10,20,30,40]
b=[50,60,70,80]
print(a[3])
print(a[2:3])
print(a+b)
print(a*3)
for i in a:
    print(i)
    
n= int(input("Enter Total Numbers:"))
a1=[]
for i in range(1,n+1):
    k=int(input("Enter The Number:"))
    a1.append(k)
print("Your List Is:",a1)
print("The Square of Those Elements:")
for i in a1:
    print(i*i)#square of List elements




#Odd Even List
num=[]    
even=[]
odd=[]
print("Please Enter 10 Numbers")
for t in range(1,11):
    r= int(input("Enter The Number :"))
    num.append(r)
for j in num:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The Even Numbers Are:",even)
print("The Odd Numbers Are:",odd)




#Lists Equal or Not
n1= int(input("Enter Number Of Elements In First List:"))
n2= int(input("Enter Number Of Elements In Second List:"))
l1=[]
l2=[]
l3=[]
for x in range(1,n1+1):
    k1=int(input("Enter The Element For List 1:"))
    l1.append(k1)
for x in range(1,n2+1):
    k2=int(input("Enter The Element For List 2:"))
    l2.append(k2)
print("The First List Is:", l1)
print("The Second List Is:", l2)
m=0
n=0
for x in l1:
    for y in l2:
        if(l1[m]==l2[n]):
            if(x==y):
                l3.append(i)
if(len(l1)==len(l3)):
    print("The Lists Are Equal")
else:
    print("The Lists Are Not Equal")
