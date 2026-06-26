class TreeType:
    """
    Flyweight class (Intrinsic State)
    Shared by many Tree objects.
    """

    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(
            f"Drawing {self.name} tree "
            f"(Color={self.color}, Texture={self.texture}) "
            f"at ({x}, {y}) on {canvas}"
        )


class TreeFactory:
    """
    Flyweight Factory
    Creates TreeType objects only once.
    """

    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):

        key = (name, color, texture)

        if key not in TreeFactory._tree_types:
            print(f"Creating new TreeType: {key}")
            TreeFactory._tree_types[key] = TreeType(
                name,
                color,
                texture,
            )

        else:
            print(f"Reusing existing TreeType: {key}")

        return TreeFactory._tree_types[key]


class Tree:
    """
    Context class (Extrinsic State)
    """

    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)


class Forest:

    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):

        tree_type = TreeFactory.get_tree_type(
            name,
            color,
            texture,
        )

        tree = Tree(x, y, tree_type)

        self.trees.append(tree)

    def draw(self, canvas):

        for tree in self.trees:
            tree.draw(canvas)


# -------------------------
# Client
# -------------------------

forest = Forest()

forest.plant_tree(10, 20, "Oak", "Green", "oak.png")
forest.plant_tree(30, 40, "Oak", "Green", "oak.png")
forest.plant_tree(50, 60, "Pine", "Dark Green", "pine.png")
forest.plant_tree(70, 80, "Oak", "Green", "oak.png")

print("\nDrawing Forest\n")

forest.draw("Game Canvas")