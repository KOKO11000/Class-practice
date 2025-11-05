#           Single Responsibility
class Book:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.ahutor = author
        self.content = content

    def __str__(self):
        return f"name:{self.title}, aunthor: {self.ahutor}, \n constat: {self.content}"


class ListSaving:
    def __init__(self):
        self.saver_books  = []

    def save_to_list(self, book):
        self.saver_books.append(book)
        print(book)


book1 = Book("title","Netanel", "אני אוהב את החיים ואני שמח שאני חי עם אישה כזו והילדים האלו הלוואי בה' יתן לי רק טוב כל הזמן ")
save_book = ListSaving()
save_book.save_to_list(book1)



# ================================================================
 


class Student:
    def __init__(self, name, grades: list[int]):
        self.name = name
        self.grandes = grades
    
   

class GradeCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_average(grades):
        return sum(grades) / len(grades)

s = Student("momo", [98,65,100])
calc_grades = GradeCalculator()
print(calc_grades.calculate_average(s.grandes))


# ================================================================


class Order:
    def __init__(self, items: list[str], total_price: str):
        self.items = items
        self.total_price = total_price

    def __repr__(self):
        return f"item: {self.items} \ntotal price: {self.total_price}"


class Printing:
    def __init__(self):        
        pass

    def print_invoice(self, item ):
        print(item)

items1 = ["lol", "kok","gol"]
buing = Order(items1, 528.90)
invoice = Printing()
invoice.print_invoice(buing)


# =====================================================================

#               Open/Close
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_area = shape_type
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, shape_type, radius):
        super().__init__(shape_type)
        self.radius = radius

    def area(self):
        return pi * self.radius**2
    
class Square(Shape):
    def __init__(self, shape_type, side):
        super().__init__(shape_type)
        self.side = side

    def area(self):
        return self.side**2
        
class Rectangle(Shape):
    def __init__(self, shape_type, width, height):
        super().__init__(shape_type)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    


#======================================================================================


class Notifier(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def send(self):
        pass

class EmailNotifier(Notifier):
    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def send(self):
        return "you get a MailMessage"

class SMSNotifier(Notifier):
    def __init__(self, message):
        super().__init__()
        self.message = message
    
    def send(self):
        return "you get a SMSMessage" 

class PushNotifier(Notifier):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def send(self):
        return "your pushed message"
    

# ========================================================================

#       Liskov in Action
class BirdUnit(ABC):
    def __init__(self):
        pass

    def fly(self):
        return "That bird can fly"
    

class Drone(BirdUnit):
    def __init__(self):
        super().__init__()

    def fly(self):
        return "That Unit can fly"


class GroundUnit(ABC):
    def __init__(self):
        pass
    
    def ground(self):
        return "That uint can't fly"        


class Tank(BirdUnit):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def gound(self):
        return "Tanks can't fly"
    
# ==================================================================================

#           Interface Segregation Principle
class Soldier(ABC):
    def __init__(self):
        pass

class Shooter(Soldier):
    def __init__(self):
        super().__init__()
    def infantry(self):
        return "he can shooter"
    def airSupportCaller(self):
        return "he can shoot"


class Navigator(Shooter):
    def __init__(self):
            super().__init__()
    def infantry(self):
        return "he can shooter"


# class AirSupportCaller(Soldier):
#     def __init__(self):
#         super().__init__()

#     def 
class Infantry(Shooter):
    def __init__(self):
        super().__init__()
    
class ForwardObserver(Soldier):
    def __init__(self):
        super().__init__()

class Pilot(Soldier):
    def __init__(self):
        super().__init__()


