# with instance variable in to classes
class a:
    a=10
    def __init__(self,p):
        self.p=p
    def det_a(self):
        print("hai",self.p)
class b(a):
    def __init__(self, q):
        self.q=q
    def det_b(self):
        print(self.q)     
obj1=a("dhanush")
obj=b(10)   
print(obj1.a)
obj1.det_a()