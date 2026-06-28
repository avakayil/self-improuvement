from abc import ABC, abstractmethod


# =====================================
# Strategy Interface
# =====================================

class Strategy(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass


# =====================================
# Concrete Strategies
# =====================================

class AddStrategy(Strategy):

    def execute(self, a, b):
        return a + b


class SubtractStrategy(Strategy):

    def execute(self, a, b):
        return a - b


class MultiplyStrategy(Strategy):

    def execute(self, a, b):
        return a * b


# =====================================
# Context
# =====================================

class Context:

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):

        if self.strategy is None:
            raise Exception("Strategy not set")

        return self.strategy.execute(a, b)


# =====================================
# Client
# =====================================

context = Context()

context.set_strategy(AddStrategy())

print(context.execute_strategy(10, 5))

context.set_strategy(SubtractStrategy())

print(context.execute_strategy(10, 5))

context.set_strategy(MultiplyStrategy())

print(context.execute_strategy(10, 5))