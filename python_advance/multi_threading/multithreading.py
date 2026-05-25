import threading
import time

def number(n):
    while True:
        print(f"The current number is {n}")
        n=n+1
        time.sleep(0.5)
        if n>=27:
            break

def character():
    val=65
    while True:
        print(f"The character is {chr(val)}")
        val+=1
        time.sleep(0.5)
        if val>=ord('Z')+1:
            break


t1=threading.Thread(target=number,args=(1,))
t2=threading.Thread(target=character)


t1.start()
t2.start()

#To check weather threading is till isalive
if t1.is_alive():print("The thread t1 is still active")
if t2.is_alive():print("The thread t2 is still active")

t1.join()
t2.join()

#thread name by using getname()

print("The thread name is: ",t1.getName())
print("The thread name is: ",t2.getName())


#thread setting new name setname()

t1.setName("The_Number")
t2.setName("The_character")

print("The thread name is: ",t1.getName())
print("The thread name is: ",t2.getName())


