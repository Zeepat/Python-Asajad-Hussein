class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Shape({self.x}, {self.y})"

    def __str__(self):
        return f"A shape at ({self.x}, {self.y})"