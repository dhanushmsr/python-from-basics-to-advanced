class stack():
    def __init__(self):
        self.stack=[]

    def push(self,push):
        self.stack.append(push)
    
    def pop(self):
        return self.stack.pop()
    
    def peak(self):
        return self.stack[-1]
    
    def display(self):
        print(self.stack)
    
obj=stack()
obj.push(10)
obj.push(15)
obj.push(1)
obj.push(30)
obj.pop()  #Work based on the Principle of First in Last out(FILO | LIFO )
print(obj.peak())
obj.display()
    



