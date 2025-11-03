import math
from abc import ABC, abstractmethod
class Shape_Area_calculation(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape_Area_calculation):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):        
        return self.width * self.height
    
class Circle(Shape_Area_calculation):
    def __init__(self, r):
        self.r = r 

    def area(self):        
        return math.pi * self.r**2


c1 = Circle(5)
r1 = Rectangle(5,5)

print(c1.area())
print(r1.area())

