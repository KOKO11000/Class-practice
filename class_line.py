import math
class Point:
    count = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.count += 1

    def __del__(self):
        Point.count -= 1

    def show(self):
        print(f"({self.x},{self.y})")

    @staticmethod
    def distance(p1, p2):
        dx = p1.x - p1.x
        dy = p1.y - p2.y
        return (dx**2 + dy**2) ** 0.5





class Line:
    counter = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        Line.counter += 1

    def show(self):
        print(self.a, self.b)
    
    def length(self):
        print(math.dist(self.a, self.b))

    @classmethod
    def how_many(cls):
        print(cls.counter)

    @staticmethod
    def is_horizontal(line):
        if line.a.y == line.b.y:
            return True
        else: 
            return False
    
    @staticmethod
    def is_vertical(line):
        if line.a.x == line.b.x:
            return True
        else:
            return False
        
if __name__ == "__main__":
    # print(Point.count)
    p1  = Point(4,5)
    p2 = Point(4, 6)
    p3 = Point(4, 6)
    p4 = Point(2,4)
    l =  Line(p1, p2)
    l1= Line(p2, p3)
    l2 = Line(p3, p4)
    l3 = Line(p3, p4)
    p4 = Line(p4, p4)
    print(Line.how_many())
    print(l.is_horizontal(l))
    print(l.is_vertical(l))
    print(Point.count)
    print(Line.counter)
    print(Point.distance(p1, p2))
    print(Point.show(p1))
