class naturalno:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<=self.stop:
            res=self.start
            self.start+=1
            return res
        else:
            raise StopIteration

obj=naturalno(10,20)
print(obj)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))