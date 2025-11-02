class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        

    def area(self):
        return self.width * self.heigth
    
    def perimeter(self):
        return 2 * (self.width + self.heigth)
    

surface = Rectangle(5,5)
print(surface.area())
print(surface.perimeter())