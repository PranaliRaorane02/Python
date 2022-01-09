#Lists
#Kindly run each program separately as they have repreated variables.

#Addition Of Two Lists
n5= int(input("Enter Number Of Elements In First List:"))
n7= int(input("Enter Number Of Elements In Second List:"))
lt1=[]
lt2=[]
lt3=[]
sum=0
for i in range(n5):
    kt1=int(input("Enter The Element For List 1:"))
    lt1.append(kt1)
for q in range(n7):
    kt2=int(input("Enter The Element For List 2:"))
    lt2.append(kt2)
print("The First List Is:", lt1)
print("The Second List Is:", lt2)
if(n5==n7):
     for q in range(n5):
         sum=lt1[q]+lt2[q]
         lt3.append(sum)
else:
    print("The Number Of Elements Are Unequal, Hence Cannot Add")
print("The Addition Of The Two Lists Is:", lt3)


#Common List Elements
nc1= int(input("Enter Number Of Elements In First List:"))
nc2= int(input("Enter Number Of Elements In Second List:"))
lc1=[]
lc2=[]
lc3=[]
for y in range(1,nc1+1):
    kc1=int(input("Enter The Element For List 1:"))
    lc1.append(kc1)
for y in range(1,nc2+1):
    kc2=int(input("Enter The Element For List 2:"))
    lc2.append(kc2)
print("The First List Is:", lc1)
print("The Second List Is:", lc2)
for y in lc1:
    for z in lc2:
            if(y==z):
                lc3.append(y)
print("The Common Elements Are:", lc3)


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
