from abc import ABC, abstractmethod


# ==================================
# Component
# ==================================

class Graphic(ABC):

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass


# ==================================
# Leaf
# ==================================

class Dot(Graphic):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        print(f"Dot at ({self.x}, {self.y})")


class Circle(Dot):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(
            f"Circle at ({self.x}, {self.y}), Radius = {self.radius}"
        )


# ==================================
# Composite
# ==================================

class CompoundGraphic(Graphic):

    def __init__(self):
        self.children = []

    def add(self, child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.remove(child)

    def move(self, dx, dy):
        for child in self.children:
            child.move(dx, dy)

    def draw(self):
        print("\nDrawing Compound Graphic")

        for child in self.children:
            child.draw()


# ==================================
# Client
# ==================================

all_shapes = CompoundGraphic()

dot = Dot(1, 2)
circle = Circle(5, 3, 10)

all_shapes.add(dot)
all_shapes.add(circle)

print("Before Moving")
all_shapes.draw()

print("\nAfter Moving")
all_shapes.move(10, 10)
all_shapes.draw()