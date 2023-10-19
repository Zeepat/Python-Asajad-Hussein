import math
class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, change_in_x, change_in_y):
        if (type(change_in_x) == int or type(change_in_x) == float) and (type(change_in_y) == int or type(change_in_y) == float):
            self.x += change_in_x
            self.y += change_in_y
        else:
            raise ValueError("The translation in x and y has to be an integer or float.")

    def __repr__(self):
        return f"Shape({self.x}, {self.y})"

    def __str__(self):
        return f"A shape at ({self.x}, {self.y})"
    
class Rectangle(Shape):
    def __init__(self, x = 0, y = 0, side1 = 1, side2 = 1):
        if side1 <= 0 or side2 <= 0:
            raise ValueError("The side1 and side2 of the rectangle must be positive.")
        self.side1 = side1
        self.side2 = side2
        self.x = x
        self.y = y
    
    @property
    def area(self):
        return self.side1 * self.side2
    
    @property
    def circumference(self):
        return 2 * (self.side1 + self.side2)
    
    def is_square(self):
        return self.side1 == self.side2
    
    def __repr__(self):
        return f"Rectangle({self.side1}, {self.side2}, x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"A rectangle with side1 {self.side1} and side2 {self.side2} at ({self.x}, {self.y})"
    
class Circle(Shape):
    def __init__(self, x = 0, y = 0, radius = 1):
        if radius <= 0:
            raise ValueError("The radius of the circle must be positive.")
        self.radius = radius
        self.x = x
        self.y = y

    @property
    def area(self):
        return self.radius**2 * math.pi 
    
    @property
    def circumference(self):
        return 2 * self.radius * math.pi

    def is_unit_circle(self):
        return self.x == 0 and self.y == 0 and self.radius == 1
    
    def __repr__(self):
        return f"Circle({self.radius}, x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"A circle with radius {self.radius} at ({self.x}, {self.y})"