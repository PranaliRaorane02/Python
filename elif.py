#Simple elif programs

#Three Numbers
num1= int(input("Enter the First Number:"))
num2= int(input("Enter the Second Number:"))
num3= int(input("Enter the Third Number:"))
if(num1>num2 and num1>num3):
    print("The Greatest Number is:", num1)
elif(num2>num1 and num2>num3):
    print("The Greatest Number is:", num2)
elif(num3>num1 and num3>num2):
    print("The Greatest Number is:", num3)
elif(num1==num2 and num2==num3 and num1==num3):
     print("All Numbers are Equal")
elif(num1==num2):
    print("The first two Numbers are equal")
elif(num1==num3):
    print("The first and third Numbers are equal")
elif(num2==num3):
    print("The last two Numbers are equal")

#Percentage
a= int(input("Enter you percentage:"))
if(a>=75):
    print("Distinction")
elif(a>=60 and a<75):
    print("First Class")
elif(a>=45 and a<=59):
    print("Second Class")
elif(a>=35 and a<=44):
    print("Pass Class")
else:
    print("Sorry Fail")
