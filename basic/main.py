def dhanush(age):
    if age>=60:
        return "senior citizen"
    elif age>=18:
        return "eligible"
    else:
        return "not Eligible"
name=int(input("enter a number"))
print(dhanush(name))
