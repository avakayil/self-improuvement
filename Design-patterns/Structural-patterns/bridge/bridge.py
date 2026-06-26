from abc import ABC, abstractmethod


# ==================================
# Implementation Hierarchy
# ==================================

class Device(ABC):

    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


# ==================================
# Concrete Implementations
# ==================================

class TV(Device):

    def __init__(self):
        self.power = False
        self.volume = 50
        self.channel = 1

    def is_enabled(self):
        return self.power

    def enable(self):
        self.power = True
        print("TV ON")

    def disable(self):
        self.power = False
        print("TV OFF")

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        print(f"TV Volume: {self.volume}")

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        print(f"TV Channel: {self.channel}")


class Radio(Device):

    def __init__(self):
        self.power = False
        self.volume = 30
        self.channel = 101

    def is_enabled(self):
        return self.power

    def enable(self):
        self.power = True
        print("Radio ON")

    def disable(self):
        self.power = False
        print("Radio OFF")

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        print(f"Radio Volume: {self.volume}")

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        print(f"Radio Channel: {self.channel}")


# ==================================
# Abstraction Hierarchy
# ==================================

class RemoteControl:

    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(
            self.device.get_volume() + 10
        )

    def volume_down(self):
        self.device.set_volume(
            self.device.get_volume() - 10
        )

    def channel_up(self):
        self.device.set_channel(
            self.device.get_channel() + 1
        )

    def channel_down(self):
        self.device.set_channel(
            self.device.get_channel() - 1
        )


# ==================================
# Refined Abstraction
# ==================================

class AdvancedRemoteControl(RemoteControl):

    def mute(self):
        self.device.set_volume(0)


# ==================================
# Client
# ==================================

tv = TV()

remote = RemoteControl(tv)

remote.toggle_power()
remote.volume_up()
remote.channel_up()


print()

radio = Radio()

advanced = AdvancedRemoteControl(radio)

advanced.toggle_power()
advanced.volume_up()
advanced.mute()