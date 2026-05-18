if __name__=="__main__":
    n=int(input("Enter the Number: "))
    if n>=-9 and n<=9:
        print("single digit")
    elif (n>=-99 and n<=-9 ) or (n>=10 and n<=99):
        print("double digit") 
    elif (n>=-999 and n<=-99 ) or (n>=100 and n<=999):
        print("trible digit") 
    else:
        print("undefiend")