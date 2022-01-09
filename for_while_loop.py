#LOOPS
#Kindly run all the programs separately as they have similar variables.

# Numbers Divisible by 7 and 5 between 1500-2700
for i in range(1500,2701):
    if(i%7==0 and i%5==0):
        print(i)
        
        
#Average Of n Numbers
r= int(input("How Many Numbers Do You Want To Average?"))       
avg=0
sum=0
for i in range(1,r+1):
    n=int(input("Enter The Number:"))
    sum=sum+n
    avg=sum/r
print("The Average Of The",r,"Numbers Is:", avg)


#Sum Of Square Of Digits
n=int(input("Enter The Number:"))
sum=0
while(n>0):
    r=n%10
    sum=sum+(r*r)
    n=n//10
print("Sum Of Square Of The Digits Of The Number Are:",sum)

#Reverse of A Number
n=int(input("Enter The Number:"))
rev=0
while(n>0):
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("Reverse Of The Digits Is:",rev)


#1/1+1/2+1/3+..........+1/n
n=int(input("Enter The Last Number Of Series:"))
sum=0
for i in range(1,n+1):
    sum=sum+(1/i)
print("The Sum Of The Series Is:", sum)

#Multiplication Of Digits Of Number
n=int(input("Enter The Number:"))
m=1
while(n>0):
    r=n%10
    m=m*r
    n=n//10
print("Product Of The Digits Of The Number Are:",m)

#Sum of Even Digits, Product Of Odd Digits
n=int(input("Enter The Number:"))
prdct=1
add=0
while(n>0):
    r=n%10
    n=n//10
    if(r%2==0):
        prdct=prdct*r
    if(r%2!=0):
        add=add+r
print("Sum Of Odd Digits Is:",add)
print("Product Of Even Digits Is:",prdct)

#Factorization
n= int(input("Enter The Number:"))
for i in range(1,n+1):
    if(n%i==0):
       print(i)
        
       
#Greatest Common Divisor
n1= int(input("Enter The First Number:"))
n2= int(input("Enter The Second Number:"))
mult=1
for i in range(1,n1+1):
    if(n1%i==0 and n2%i==0):
       mult= mult*i
print(mult)
