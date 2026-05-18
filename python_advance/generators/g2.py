def eight_table(last):
    for i in range(last):
        yield i,i*8
res=eight_table(int(input("enter the value that you want till of 8th table: ")))
print(res)
for i in res:
    print(f'{i[0]}*8={i[1]}')
