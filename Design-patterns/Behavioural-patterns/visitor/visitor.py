from abc import ABC, abstractmethod


# ======================================
# Visitor Interface
# ======================================

class Visitor(ABC):

    @abstractmethod
    def visit_dot(self, dot):
        pass

    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


# ======================================
# Shape Interface
# ======================================

class Shape(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# ======================================
# Concrete Shapes
# ======================================

class Dot(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def accept(self, visitor):
        visitor.visit_dot(self)


class Circle(Shape):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)


# ======================================
# Concrete Visitor
# ======================================

class XMLExportVisitor(Visitor):

    def visit_dot(self, dot):

        print(
            f"<dot x='{dot.x}' y='{dot.y}'/>"
        )

    def visit_circle(self, circle):

        print(
            f"<circle x='{circle.x}' "
            f"y='{circle.y}' "
            f"radius='{circle.radius}'/>"
        )

    def visit_rectangle(self, rectangle):

        print(
            f"<rectangle width='{rectangle.width}' "
            f"height='{rectangle.height}'/>"
        )


# ======================================
# Client
# ======================================

shapes = [

    Dot(2, 3),

    Circle(5, 5, 10),

    Rectangle(20, 30)

]

visitor = XMLExportVisitor()

for shape in shapes:

    shape.accept(visitor)