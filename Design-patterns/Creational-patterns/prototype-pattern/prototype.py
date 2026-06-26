from abc import ABC,abstractmethod


#prototype
class Shape(ABC):
    def __init__(self,source=None):
        if source:
            self.x=source.x
            self.y=source.y
            self.color = source.color
        else:
            self.x=0
            self.y=0
            self.color = "Black"
    @abstractmethod
    def clone(self):
        pass


class Rectangle(Shape):
    def __init__(self,sorce=None):
        super.__init__(sorce)

        if sorce:
            self.width = sorce.width
            self.height = sorce.height
        else:
            self.width =0
            self.height = 0
    def clone(self):
        return Rectangle(self)
    
class Circle(Shape):
    def __init__(self, source=None):
        super().__init__(source)
    
        if source:
            self.radius = source.radius
        else :
            self.radius =0
    def clone(self):
        return Circle(self)


#client

shapes =[]
circle = Circle()
circle.x = 10
circle.y = 20
circle.color = "Red"

shapes.append(circle)

another_circle = circle.clone()
shapes.append(another_circle)

for shape in shapes:
    print(shape)


