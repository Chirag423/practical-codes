a=input('enter the string :- ')
b=input('enter the letter you want to remove :- ')

while True:
    i=a.index(b)
    a=(a[:i]+a[i+1:])
print(a)
