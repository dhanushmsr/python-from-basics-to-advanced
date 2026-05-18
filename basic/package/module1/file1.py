# access specifier (public i.e., the variable declared without any underscore at prefix)
#protected i.e., the variable declared with one underscore at prefix
#private i.e., the variable declared with double underscore at prefix

class bus:
    bus_no="TN-69-CM-2026"
    owner="Thalapathy"

    def __init__(self,p_name, travel_date,price):
        self.p_name=p_name
        self.travel_date=travel_date
        self.price=price
    def detail(self):
        print(f"I am {self.p_name} travel on the date of {self.travel_date} for the price amount {self.price} on the bus number {bus.bus_no} and it's owners name is {bus.owner}")
obj=bus("dhanush",'13-april-26',449)
bus.detail(obj)