op=input("Enter the operation that you want \naddition \t subtraction \t muliplication \t division \t modular division \t floor division: \n ")
op1=op.lower()
match op1:
    case _ if op1 in ['additions','addition','add']:
        n=int(input("enter operand_1:"))
        n1=int(input("enter operand_2:"))
        print("additions of two number is " ,n+n1)
    case _ if op1 in ['subtraction','subtractions','subtract']:
        n=int(input("enter operand_1:"))
        n1=int(input("enter operand_2:"))
        print("difference of two number is " ,n-n1)
    case _ if op1 in ['division','divisions','divide']:
        n=int(input("enter operand_1:"))
        n1=int(input("enter operand_2:"))
        print("division of two number is " ,n/n1)
    case _ if op1 in ['multiplications','muliplication','multiply']:
        n=int(input("enter operand_1:"))
        n1=int(input("enter operand_2:"))
        print("product of two number is " ,n*n1)
    case _:
    
        print("invalid")