# class train:
#     train_no=1504
#     train_name="bharath"
#     def __init__(self,p_name,tra_date,ticket_price,From,to):
#         self.p_name=p_name
#         self.tra_date=tra_date
#         self.ticket_price=ticket_price
#         self.From=From
#         self.to=to
#     def detail(self):
#         print(f"The passenger name is {self.p_name} traveling from {self.From} to {self.to} on {self.tra_date} with the price ammount {self.ticket_price} in Train number {train.train_no} and the name is {self.train_name} ")
# obj=train("dhanush","05-04-2026", 145,'madiwala','coimbatore')
# obj2=train("aswin","12-april-2026",160,'KSR','CBE')
# train.detail(obj)
# obj2.detail()



class Student:
    address = 'musiri'

    def __init__(self, name, age, yop, mno):
        self.name = name
        self.age = age
        self.yop = yop
        self.mno = mno

    def detail(self):
        print(f'Student name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Year of passing is {self.yop}')
        print(f'Mobile number is {self.mno}')
        print(f'Address is {Student.address}')
s1 = Student("kumar", 20, 2026, 9876543210)
s2 = Student("loki_man", 26, 2027, 9566315428)

s1.detail()


