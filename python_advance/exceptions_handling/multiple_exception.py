try:
    a=float(input("Enter the number: "))
    b=float(input("Enter the number: "))
    c=a/b
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde: #we can also perform like except (ValueError, ZeroDivisionError) as all: to handle mutlitple at once 
    print(zde)
else:
    print(c)
