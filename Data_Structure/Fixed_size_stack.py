from stack import stack
class fixed_size_stack(stack):
    def __init__(self,max_size):
        super().__init__()
        self.max_size=max_size
    
    def isempty(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("stack is non empty")
    def isfull(self):
        if len(self.stack)==self.max_size:
            print("stack is full")
        else:
            print("stack is not full")

    def push(self,push):
        if len(self.stack)<self.max_size:
            self.stack.append(push)
            print("stack is pushed successfully")

        else:
            print("stack is overflow")
    
    def pop(self):
        if len(self.stack)==0:
            print("stack is underflow")
        else:
            print(self.stack.pop())

    
obj1=fixed_size_stack(5)
obj1.push(6)
obj1.push(10)
obj1.push(0.1)
obj1.push(1)
obj1.push(11)
obj1.push(45)
obj1.push(32)
obj1.display()
            
