n=input("enter a character")
if len(n)==1:
    if (ord(n)>=97 and ord(n)<=122) or (ord(n)>=65 and ord(n)<=90):
        print("enter input is albhabet")
    else:
        print("not an albhabet")

else:
    print("invalid input")
