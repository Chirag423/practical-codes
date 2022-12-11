t1=(1,2,5,7,9,2,4,6,8,10)
a=int(len(t1))
b=int(a/2)

for i in range(0,b):
     print(t1[i],end=',')
print(' ')
        
        
for i in range(b,a):
    print(t1[i],end=',')
print('')    
x=[]
for i in t1:
    if i%2==0:
        x.append(i)
x=tuple(x)
print (x)
