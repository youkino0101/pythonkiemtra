from shape.Shape import Shape
import math
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def chuVi(self):
        return self.a + self.b + self.c
    
    def dienTich(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))