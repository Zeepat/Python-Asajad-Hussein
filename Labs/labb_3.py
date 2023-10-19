class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Shape({self.x}, {self.y})"

    def __str__(self):
        return f"A shape at ({self.x}, {self.y})"
    
class Rectangle(Shape):
    def __init__(self, x = 0, y = 0, side1 = 1, side2 = 1):
        self.side1 = side1
        self.side2 = side2
        self.x = x
        self.y = y