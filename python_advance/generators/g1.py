def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        temp=a
        a=b
        b=a+temp
res=fibonacci(10)
print(res)
for i in res:
    print(i)