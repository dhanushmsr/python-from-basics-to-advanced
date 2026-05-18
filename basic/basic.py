# a=10.5
# b=3
# print(a//b) #floor division (round of lower value) output:3.0
# help()
# b=3
# print(a//b)      #floor division (round of lower value) output:-4 why because of -4 is lower than -3 
# a=4+5j           #complex data type
# b=2
# print(a*b)
# c="mss "
# print(b*c,)
# a=(input("enter a number"))
# b=int(float(a))
# print(b,type(b))             #output Enter a number " " <class 'str'> by default it gets string as a input to get int,float,bool we use typecasting
# a=bool(input("Value:"))            
# print(a,type(a))                   #Value:False \n True <class 'bool'> in boolean execept (0, empty space and empyt set"[]") all other or True
a=10.1
b=10.1
# print(a,~b)
print(a is b)
print(a is not b)
c=[10,20,0]
print(10 in c)
print (10 not in c)