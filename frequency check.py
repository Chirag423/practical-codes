x=str(input('enter a string :- '))
y={}
for i in x:
    if i in y:
        y[i]+=1
    else:
        y[i]=1
print('count of all characters in',x,'is :-\n',str(y))
