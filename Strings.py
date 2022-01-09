#Username and Password
un= str(input("Enter The Username:"))
pw= str(input("Enter The Password:"))
if(un=="admin" and pw=="admin"):
    print("LOGIN SUCCESSFUL")
if(un=="admin"):
    if(pw!="admin"):
        print("VALID USERNAME BUT INVALID PASSWORD, LOGIN FAIL")
if(pw=="admin"):
    if(un!="admin"):
        print("VALID PASSWORD BUT INVALID USERNAME, LOGIN FAIL")
if(un!="admin" and pw!="admin"):
    print("INVALID USERNAME AND PASSWORD, LOGIN FAIL")

#Q1. Strings Equal or Not
s1= str(input("Enter the First String:"))
s2= str(input("Enter the Second String:"))
if(s1==s2):
    print("The Strings are Equal")
else:
    print("The Strings are Not Equal")
    
    
#String Basics
s12= "HELLO "
s13= "WORLD"
print(s12[::-1])
print(s12+s13)
print(s12*5)
print(len(s12))
print('s' in s12)

w1= "c:// Windows"
print(w1)
w2= '''#They said," Hello How Are You?"'''
print(w2)
for i in w2:
    print(i)
    
str= "WELCOME"
print(str[-7])
print(len(str))
