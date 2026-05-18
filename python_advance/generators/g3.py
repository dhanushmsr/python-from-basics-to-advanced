def reg_no(institue, year, course):
    num=1
    while True:
        reg=str(num)+institue[0:2]+str(year)+course
        yield reg.upper()
        num+=1
res=reg_no(input("Enter your institute name: "),int(input("enter your year of passout: ")), input("enter your course name in short form: "))
repeat=0
while True:
    match(repeat):
        case 0:
            print(next(res))
        case 1:
            print("Program is End")
            exit()
        case _:
            print("invalid input")
    repeat=int(input("enter 0 for next register number, 1 for exit the program: "))