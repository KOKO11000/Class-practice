from abc import ABC, abstractmethod
class Ticket(ABC):
    def __init__(self, destination, base_price):
        self.destination = destination
        self.base_price = base_price
        
    @abstractmethod    
    def price(self):
        pass    
class BusTicket(Ticket):
    def price(self):
        return f"destintion: {self.destination}, price: {self.base_price}$"

class TrainTicket(Ticket):
    def price(self):
        super().price()
        self.base_price += 10
        return f"destintion: {self.destination}, price: {self.base_price}$"

class FlightTicket(Ticket):
    def price(self):
        super().price() 
        self.base_price += 100
        return f"destintion: {self.destination}, price: {self.base_price}$"
    
bus = BusTicket("Jerusalem", 8)
train = TrainTicket("Haifa",8)
flight = FlightTicket("Cyiprus",8)

print(bus.price())
print(train.price())
print(flight.price())