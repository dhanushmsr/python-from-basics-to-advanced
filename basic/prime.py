n=int(input("n: "))
c=0
if n<=1:
    print("negative or not prime number")
else:
    for i in range(2,n,1):
        if n%i==0:
            c=c+1
    if c ==0:
        print("prime number")
    else:
        print("not a prime")