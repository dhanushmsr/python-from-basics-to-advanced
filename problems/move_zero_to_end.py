def move_zero_to_end(l):
    l1=list(l)
    n=len(l1)
    for i in range(n):
        # if len(l1[i])<1:
        #     for i in range(len(l1[i])):
        #         if l1[i] ==0:
        #             l1.pop(i)
        #             l1.append(0)
        if l1[i] ==0:
            l1.pop(i)
            l1.append(0)
    return l1

print(move_zero_to_end([2,3,0,1,3,[0,10],1,0,10]))
