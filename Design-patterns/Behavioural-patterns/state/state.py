from abc import ABC, abstractmethod


# =====================================
# State Interface
# =====================================

class State(ABC):

    @abstractmethod
    def next(self, light):
        pass

    @abstractmethod
    def action(self):
        pass


# =====================================
# Concrete States
# =====================================

class RedState(State):

    def next(self, light):
        light.state = GreenState()

    def action(self):
        print("RED -> STOP")


class GreenState(State):

    def next(self, light):
        light.state = YellowState()

    def action(self):
        print("GREEN -> GO")


class YellowState(State):

    def next(self, light):
        light.state = RedState()

    def action(self):
        print("YELLOW -> SLOW DOWN")


# =====================================
# Context
# =====================================

class TrafficLight:

    def __init__(self):
        self.state = RedState()

    def change(self):
        self.state.next(self)

    def show(self):
        self.state.action()


# =====================================
# Client
# =====================================

light = TrafficLight()

light.show()

light.change()

light.show()

light.change()

light.show()

light.change()

light.show()