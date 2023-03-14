from shape.Shape import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def chuVi(self):
        return 2 * 3.14 * self.radius
    
    def dienTich(self):
        return 3.14 * self.radius ** 2