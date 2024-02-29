class shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate__area(self):
        return self.width*self.height
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate__area(self):
        totalarea=0
        for shape in shape:
            totalarea+=shape.calculate
