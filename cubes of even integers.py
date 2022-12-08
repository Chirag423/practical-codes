a=[]
x=[]
b= int(input("number of numbers you want to insert"))
for i in range(0,b):
    c=int(input("enter your integer"))
    a.append(c)
for i in a:
    if i%2==0:
        z=i**3
        x.append(z)
print(x)        
    
