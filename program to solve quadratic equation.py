import cmath
a = float(input("enter value of a :- "))
b = float(input("enter value of b :- "))
c = float(input("enter value of c :- "))
d=b**2-4*a*c
sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)
print("solutions are :- ",sol1,"and",sol2)


while True:
    x=input("To continue press 'Y', to exit press any key ")
    if x=='Y' or x=='y':
        a = float(input("enter value of a :- "))
        b = float(input("enter value of b :- "))
        c = float(input("enter value of c :- "))
        d=b**2-4*a*c
        sol1 = (-b+cmath.sqrt(d))/(2*a)
        sol2 = (-b-cmath.sqrt(d))/(2*a)
        print("solutions are :- ",sol1,"and",sol2)
    else:
        print("program is over")

        break
