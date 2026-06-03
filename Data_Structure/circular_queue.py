class circular_queue:
    def __init__(self,max):

        self.maxSize=max
        self.q=[None]*max
        self.front=-1
        self.rear=-1


    def is_full(self):
        if  self.front==0 and self.rear+1==self.maxSize:
            return True
        elif self.rear==self.front-1:
            return True
        else:
            return False
        
    def is_empty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else: return False

    def enqueue(self,value):
        if self.is_full():
            print("Queue is overflow")
        else:
            if self.rear+1==self.maxSize:
                self.rear=0
            else:
                self.rear+=1
                if self.front==-1:
                    self.front=0
            self.q[self.rear]=value
            print("value is added successfully")
    
    def dequeue(self):
        idx=self.front
        if self.is_empty():
            print("queue is underflow")
        else:
            if self.front==self.rear:
                self.front=-1
                self.rear=-1

            elif self.front+1==self.maxSize:
                self.front=0
            else:
                self.front+=1
                self.q[idx]=None
    
    def peak(self):
        if self.is_empty():
            print('No element to display')
        else:
            print(f"the peak value is: {self.q[self.front]}")
            
    def display(self):
        if self.is_empty():
            print("No value is there to display")
        else:
            print(self.q , "front: ", self.front ,  "rear: ",self.rear , sep="\t")

obj=circular_queue(5)

while True:
    print("************This is Circular Queue***************")

    c = int(input(
    "1 for checking full\n"
    "2 for checking empty\n"
    "3 for enqueue\n"
    "4 for dequeue\n"
    "5 for display peak\n"
    "6 for display all elements\n"
    "7 for exit\n"
    "Enter your choice: "
    ))
    match c:
        case 1:
            if obj.is_full():
                print("queue is underflow")
            else:
                print("queue is not full")
        case 2:
            if obj.is_empty():
                print("queue is empty")
            else:
                print("queue is not empty")
        case 3:
            obj.enqueue(int(input("enter the value to enqueue: ")))
            
        case 4:
            obj.dequeue()
            print("value is deleted successfully")
        
        case 5:
            obj.peak()
        
        case 6:
            obj.display()
        case 7:
            exit()
        case _:
            print("input is not valid please select as below")
    