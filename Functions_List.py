#Prime, Composite, Even Odd 
def list1(n):
    l1=[]
    even=[]
    odd=[]
    prime=[]
    comp=[]

    
    for i in range(n):
        e=int(input("Enter The Element:"))
        l1.append(e)
    for j in l1:
         if j%2==0:
            even.append(j)
         if j%2!=0:
            odd.append(j)
    for k in l1:
        c=0
        for p in range(1,k+1):
            mod=k%p
            if mod==0:
                c+=1
        if c==2:
            prime.append(k)
        if c>2:
            comp.append(k)
            
            
    print("The Even Elements Are:",even)
    print("The Odd Elements Are:",odd)
    print("The Prime Elements Are:",prime)
    print("The Composite Elements Are:",comp)
    
n=int(input("Enter The Number Of Elements:"))   

list1(n)
