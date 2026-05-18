from copy import deepcopy
l=[10,2,1,4,[6,'py',4],7]
b=deepcopy(l)
b[-2].insert(2,'sql')
print(b)
print(l)
#unlike shallow copy in nested sequeces even if we modified it won't affected on the orginal sequence