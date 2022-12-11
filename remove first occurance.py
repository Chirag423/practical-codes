a=input('enter the string :- ')
b=input('enter the letter you want to remove :- ')
i=a.index(b)
print(a[:i]+a[i+1:])
