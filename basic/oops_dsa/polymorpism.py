class vechile:
    def travel_type():
        pass
class bus(vechile):
    bus_name="A1"
    bus_type="Heavy-engine"

    def __init__(self,boarding, dropping, seat_type,paymet_src,distance):
        self.boarding=boarding
        self.dropping=dropping
        self.seat_type=seat_type
        self.paymet_src=paymet_src
        self.distance=distance
        if self.seat_type=="semi":
            self.cost=self.distance*12
        elif self.seat_type=='sleeper':
            self.cost=self.distance*10
        else:
            self.cost="Cost not defined contact bus operator"
    
    def travel_type(self):
        print(f"{'*'*6}This is {bus.bus_name} Travels{'*'*6}")
        print('Mode of Travel is Road')
        print(f'price of your travel is: {self.cost}')
    
class aeroplane(vechile):
    vechile_name="Air India"
    vechile_type='Aeroplane'

    def __init__(self, from_country, to_country, seat_type,distance):
        self.from_country=from_country
        self.to_country=to_country
        self.seat_type=seat_type
        self.distance=distance
        if self.seat_type=="semi":
            self.cost=self.distance*100
        elif self.seat_type=='sleeper':
            self.cost=self.distance*75
        else:
            self.cost="Cost not defined contact bus operator"

    def travel_type(self):
        print(f"{'*'*6}This is {aeroplane.vechile_name} AirLines{'*'*6}")
        print('Mode of Travel is Air ')
        print(f'price of your travel is: {self.cost}')


if __name__=='__main__':
    # obj1=bus('tenkasi','coimbatore','semi',"cash",210)
    # obj2=aeroplane('india','usa','sleeper',450)
    obj1=bus(input("enter The boarding point: "),input("enter the Dropping point: "),input("enter the seat type as semi or sleeper: "),input("enter the payment source: "),int(input("enter the distance in KM: ")))
    obj2=aeroplane('india','usa','sleeper',450)
    
    obj1.travel_type()
    obj2.travel_type()
            

