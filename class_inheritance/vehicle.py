class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("The vehicle is moving")

    
class Car(Vehicle):
    def override(self):
        print("The car drives")
    

class Plane(Vehicle):
    def override (self):
        print("The plane flies")


car1 = Car("brand: Toyota", "model: prius")
car2 = Car("brand: Tesla", "model: Model Y")
car3 = Car("brand: Mitsubishi", "model: Out-Lander")
plane1 = Plane("brand: Boeing", "model: 747")
plane2 = Plane("brand: Airbus", "model: B52") 

vehicle: Vehicle = [car1, car2, car3, plane1, plane2]

for vehicle in vehicle:
    print(vehicle.brand)
    print(vehicle.model)
    vehicle.override()
 