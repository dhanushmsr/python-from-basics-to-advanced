# class variables
'''class student:
    a=10
val=student()
print(val.a)
print(student.a)
print(dir(val))
print(dir(student))'''

#instance variable
'''class student:
    def __init__(self):
        self.p=10
obj=student()
print(dir(student)) 
#accessing instance vairable directly by class is not possible to access it we need to create an object. it will only load the               memory for instance variables
print(dir(obj))
# print(student.p) #attribute error
print(obj.p)'''

# Instaace method
class student:
    def fun(self):
        print("i am dhannush")
obj=student()
print(dir(student))
print(student.fun)
print(obj.fun)