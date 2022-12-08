a=int(input("enter a number "))
b=int((a-1)/2)
c=int(1)
for i in range (0,a):
    if i<=((a-1)/2):
        print(b*" ",c*"*")
        b-=1
        c+=2
    else:
        c-=2
        b+=1
        print(b*" ",c*"*")

if a%2!=0:
    print((b+1)*" ","*")
