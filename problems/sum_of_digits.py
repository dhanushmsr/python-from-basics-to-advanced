def sum_of_digit(num):
    su=0
    while num / 10 != 0:
        rem=num%10
        su=su+rem
        num=num // 10
    return su
n=int(input("Enter a number"))
print ("Sum of Number is:", sum_of_digit(n))