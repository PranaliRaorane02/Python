#Patterns
#Kindly run all the pattern programs separately

#1.Simple Right-Triangle
for i in range(1,11):
    for j in range(1,i+1):
        print(" * ", end='')
    print()
    
    
#2.
for i in range(1,6):
    for j in range(1,i+1):
        print(" $ ", end='')
    print()
    
#3.
for i in range(1,6):
    for j in range(1,i+1):
        print( "" ,j," " , end='')
    print()
    
    
#Simple Pyramid
for i in range(1,6):
    for k in range(4,i-1,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
        print( " * " , end=' ')
    print()
   

#Mirror Right Angle
for i in range(1,6):
    for k in range(4,i-1,-1):
        print(" ", end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()


#Number Pattern 1
for i in range(1,6):
    for k in range(4,i-1,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
        print( "",j,"" , end=' ')
    print()
    
#Number Pattern 2
for i in range(1,6):
    for k in range(4,i-1,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
        print( "",i,"" , end=' ')
    print()
    

#Diamond
for i in range(1,7):
    for k in range(6,i-1,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
        print(" * ", end=' ')
    print()

for p in range(1,6):
    for r in range(0,p+1):
        print(" ", end=' ')
    for q in range(5,p-1,-1):
        print(" * ", end=' ')
    print()
    
    
    
#Right Angle While Loop
i=1
while i<6:
    j=1
    while j<=i:
        print(" * ", end=' ')
        j+=1
    print()
    i+=1

#Right Angle Descending For Loop
for i in range(1,6):
    for j in range(1,i+1):
        print(" * ", end=' ')
    print()
    
   
#Right Angle For Loop
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(" * ", end=' ')
    print()
    
    
#Multiplication Table (only included because of the similar logic)
n= int(input("Enter The Number:"))
for i in range(1,11):
    mult=n*i
    print(n, "x", i, "=", mult)
    
