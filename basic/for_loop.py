# names = ["A", "B", "C"]

# for index, value in enumerate(names):
#     print(index, value)

for i in range (4,10,2): #range(start,stop,step) by default start value is 0 and step value is 1
    if i==6:
        break    #break will terminate the statement if conditions is true so the output will be 4
        continue #this will skip this part so the output is 4,8
    print(i)
    # pass keyword is used when we want to give empty statement
    if i>0:
        pass # won't affect anything