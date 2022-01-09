#Valid User
age= int(input("Enter Your Age:"))
if(age>=18):
    print("You are a valid User")
else:
    print("You are not a valid User")
 
#Greater Number
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number"))
if(num1>num2): 
    print("The Greater Number is", num1)
else:
    print("The Greater Number is", num2)

#Even or odd
num= int(input("Enter the Number:"))
if(num%2==0):
    print("The Number is Even")
else:
    print("The Number is Odd")
    
#Divisible by 3 or 7 or both
numt= int(input("Enter A Number:"))
if(numt%3==0 and numt%7==0):
    print("The Number is Divisible by Both 3 and 7")
if(numt%3==0):
    if(numt%7!=0):
      print("The Number is Divisible by 3, Not by 7")
if(numt%7==0):
    if(numt%3!=0):
      print("The Number is Divisible by 7, Not by 3 ")
if(numt%3!=0 and numt%7!=0):
    print("The Number Is Not Divisible by 3 or 7")
        
