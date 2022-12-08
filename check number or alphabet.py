
def alphabet(b):
    if b.isupper():
        print(b,'is in upper case')
        
    if b.islower():
        print(b,'is in lower case')
        
def nuber(b):
    if b==0:
        print('Zero')
    elif b==1:
        print("One")
    elif b==2:
        print('Two')
    elif b==3:
        print('three')
    elif b==4:
        print('four')
    elif b==5:
        print('five')
    elif b==6:
        print('six')
    elif b==7:
        print('seven')
    elif b==8:
        print('eight')
    elif b==9:
        print('nine')

a= input()
if a.isalpha():
    alphabet(a)
    
    
if a.isnumeric():
    number(a)
    
