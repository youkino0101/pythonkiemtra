from shape.Shape import Shape
class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def chuVi(self):
        return 2 * (self.width + self.height)
    
    def dienTich(self):
        return self.width * self.height