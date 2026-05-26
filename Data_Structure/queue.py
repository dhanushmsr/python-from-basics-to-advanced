
queue=[]
maxSize=int(input("enter the maximum size of the queue: "))
while True:
    choose=int(input("Enter 1 for enqueue \n Enter 2 for dequeue \n Enter 3 for displaying peek element \n Enter 4 for Displaying the queue \n Enter 5 to check the queue is empty \n ENter 6 to check the queue is full \n Enter 7 to exit \n Enter your the interger to perform operations in queue:"))
    match choose:
        case 1:
            if len(queue)==maxSize:
                print("the queue is overflow")
            else:
                val=eval(input("enter the value to enqueue: "))
                queue.append(val)
                print(f"{val} is added to the queue successfully")
        
        case 2:
            if len(queue)==0:
                print("the queue is underflow")
            else:
                q=queue.pop(0)
                print(f'{q} is poped successfully ')
        
        case 3:
            if len(queue)!=0:
                print(f"The peek element is {queue[0]}")
            else:
                print("queue is empty")

        case 4:
            if len(queue)!=0:
                print("the queue values are")
                print(queue)
                
            else:
                print(f"Queue is empty")         

        case 5:
            if len(queue)==0:
                print("the queue is empty")
            else:
                print("queue is not empty")
        

        case 6:
            if len(queue)==maxSize:
                print("the queue is full")
            else:
                print("the queue is not full")
        
        case 7:
            print('*'*5,"Queue operations is terminated","*"*5)
            exit()
        
        case _:
            print("operations interger is not matched re-enter the value: ")