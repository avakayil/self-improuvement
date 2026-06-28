from abc import ABC, abstractmethod


# =====================================
# Abstract Class
# =====================================

class GameAI(ABC):

    # Template Method
    def turn(self):

        self.collect_resources()

        self.build_structures()

        self.build_units()

        self.attack()

    # Default implementation
    def collect_resources(self):

        print("Collecting Resources")

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    def attack(self):

        print("Finding Enemy...")

        enemy_found = True

        if enemy_found:

            self.send_warriors()

        else:

            self.send_scouts()

    @abstractmethod
    def send_scouts(self):
        pass

    @abstractmethod
    def send_warriors(self):
        pass


# =====================================
# Concrete Class
# =====================================

class OrcAI(GameAI):

    def build_structures(self):
        print("Building Farm")
        print("Building Barracks")

    def build_units(self):
        print("Training Grunts")

    def send_scouts(self):
        print("Orc Scouts Searching")

    def send_warriors(self):
        print("Orc Warriors Attack!")


# =====================================
# Another Concrete Class
# =====================================

class MonsterAI(GameAI):

    def collect_resources(self):
        print("Monsters don't collect resources")

    def build_structures(self):
        print("Monsters don't build")

    def build_units(self):
        print("Monsters already exist")

    def send_scouts(self):
        print("Monsters wandering")

    def send_warriors(self):
        print("Monsters attack directly")


# =====================================
# Client
# =====================================

orc = OrcAI()

monster = MonsterAI()

print("----- Orc Turn -----")

orc.turn()

print()

print("----- Monster Turn -----")

monster.turn()