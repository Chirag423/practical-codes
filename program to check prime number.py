n = int(input("enter a number :- "))

if n==2 or n==3:
    if n==2:
        print("2 is a prime number ")
        print("all prime numbers till 2 are [2]")

    if n==3:
        print("3 is a prime number")
        print("all prime number till 3 are [2,3]")
else:
    for i in range (2,int(n/2)+1):
        if n%i==0:
            print (n,"is not a prime number")
            break
    else:
        print (n,"is a prime number")
    

    
    x=[2,3]
    for k in range (2,n+1):
        for j in range (2,int(k/2)+1):
            if k%j==0:
                pass
            else:
                x.append(k)
    x.remove(n)      
    print("all prime numbers till",n,"are",x)            
    
