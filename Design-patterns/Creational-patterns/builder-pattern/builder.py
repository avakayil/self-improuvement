from abc import ABC,abstractmethod

#Products
class Car:
    def __init__(self):
        self.seat = None
        self.engine = None
        self.trip_computer = None
        self.gps = None
    def show (self):
        print("the car configuration")
        print("Seatt : ",self.seat)
        print(" engine : ",self.engine)
        print(" tc : ",self.trip_computer)
        print("gps : ",self.gps)

class Manual:
    def __init__(self):
        self.instructions = []
    def show(self):
        for inst in self.instructions:
            print(" - ",inst)

#Abstract builder
class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def set_seat(self,seat):
        pass
    @abstractmethod
    def set_engine(self,engine):
        pass
    @abstractmethod
    def set_tc(self,tc):
        pass
    @abstractmethod
    def set_gps(self,gps):
        pass

#concrete builder CAR
class carBuilder(Builder):

    def __init__(self):
        self.reset()
    def reset(self):
        self.car = Car()
    def set_seat(self, seat):
        self.car.seat = seat
    def set_gps(self, gps):
        self.car.gps = gps
    def set_engine(self, engine):
        self.car.engine = engine
    def set_tc(self, tc):
        self.car.trip_computer = tc
    def get_product(self):
        product = self.car
        self.reset()
        return product
    
class ManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def set_seat(self, seats):
        self.manual.instructions.append(f"{seats} seats installed")

    def set_engine(self, engine):
        self.manual.instructions.append(f"Engine: {engine}")

    def set_tc(self, enabled):
        self.manual.instructions.append(
            "Trip Computer: Enabled" if enabled else "Trip Computer: Disabled"
        )

    def set_gps(self, enabled):
        self.manual.instructions.append(
            "GPS: Installed" if enabled else "GPS: Not Installed"
        )

    def get_product(self):
        product = self.manual
        self.reset()
        return product

#Director
class Director:
    def construct_sports_car(self,builder : Builder):
        builder.reset()
        builder.set_engine("Sport Engine")
        builder.set_gps(True)
        builder.set_seat(2)
        builder.set_tc(True)

    def construct_suv(self,builder : Builder):
        builder.reset()
        builder.set_engine("suv Engine")
        builder.set_gps(True)
        builder.set_seat(7)
        builder.set_tc(True)


#client

dir = Director()

car_builder = carBuilder()
dir.construct_sports_car(car_builder)

car = car_builder.get_product()
car.show()

manual_builder = ManualBuilder()
dir.construct_suv(manual_builder)

manual = manual_builder.get_product()
manual.show()
