class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_car_info(self):
        return f"make:{self.make}, model:{self.model}, year: {self.year}"
    
new_car = Car("Toyota", "Camery", "2025")
print("make", new_car.make)
print("model", new_car.model)
print("year", new_car.year)
print("get_car_info", new_car.get_car_info)

new_car.color = "white"
del new_car.color
print("color:", new_car.color)

