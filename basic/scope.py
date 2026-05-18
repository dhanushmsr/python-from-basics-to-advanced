def additions():
    a=10
    b=20
    c=a.__add__(b)
    print('Local ',c)
    print(locals())
    # pass
additions()
# print(locals())

# locals() function return all the local varibale and values on dict as key value pair
# global() function return all the global variables and it values on dict as key value pair
# print('outside',c) #Name error local variable cannot be accessed outside of the functions

# zip() function

print(dict(zip('dsm',[1,2,3])))