a=int(input("Enter the number:"))

# Using modular operator
# if a%2==0:
#     print(f"{a} is the even number ")
# else:
#     print(f"{a} is the odd number ")

# Using Floor division method
# if (a//2)*2==a:print(f'{a} is the even number')
# else: print(f'{a} is odd number')


# Using bitwise and operator

# if (a&1)==0:print(f'{a} is even number')
# else: print(f'{a} is odd number')

# Using Bitwise Or
# if (a|1)==a: print(f'{a} is odd number')
# else: print(f'{a} is even number')

# Using Shift operator
# if (a>>1)<<1==a: print(f'{a} is Even number')
# else: print(f'{a} is odd number')

# l=['even','odd']
# print(f'{a} is a {l[a%2]}')

d={0:'even',1:'odd'}
print(f'{a} is a {d[a%2]}')