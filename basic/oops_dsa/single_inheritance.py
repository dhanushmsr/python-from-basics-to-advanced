class train:
    train_type=input("enter the train type")
    def __init__(self,pilot,source,destinations,distance_covered):
        self.pilot=pilot
        self.source=source
        self.destinations=destinations
        self.distance=int(distance_covered)
    def train_details(self):
        if self.distance>0:
            long=self.distance
        else:
            long=200

        return(f'The train type {train.train_type} with the pilot {self.pilot} is traveling from {self.source} to {self.destinations} and the total distace cover is {long}km')
class vandha_bharath(train):
    train_no=10123
    train_name='bharath'
    def __init__(self, pilot, source, destinations, distance_covered,price,doj,NoPassanger):
        super().__init__(pilot, source, destinations, distance_covered)
        self.price=price
        self.doj=doj
        self.NoPassanger=NoPassanger
    def vandha_bharath1(self):
        print(f'The train no {self.train_no} and the train name {self.train_name} with {self.train_details()} for the price amount {self.price} with the total number of passanger {self.NoPassanger} on the date of {self.doj}')
obj=vandha_bharath('dhanush','Tenkasi','coimbatore',input("enter the total distance"),160,'12-feb-2026',input('enter the number of passanger'))
obj.vandha_bharath1()
# print(obj.train_details())