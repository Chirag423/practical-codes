print ("write string one :- ")
str1 = input()

print ("write string two :- ")
str2 = input()

print ("enter the number of characters you want to swap")
n=int(input())

x=str1[0:n]
 
str1=str1.replace(str1[0:n],str2[0:n])
 
str2=str2.replace(str2[0:n],x)

print (str1)
print (str2)
