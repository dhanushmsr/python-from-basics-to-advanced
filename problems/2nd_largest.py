def second_largest(l):
    if len(l)<2:
        return "Sequences is Not ready to read"
    max=l[0]
    second=float('-inf')
    print(second)
    for i in l:
        if i>max:
            second=max
            max=i
        elif i>second and i<max:
            second=i
    return second

l=[10,5,20,8,20,15]
print(second_largest(l))