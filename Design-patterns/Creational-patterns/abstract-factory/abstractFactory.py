from abc import ABC,abstractmethod

#abstract products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def paint(self):
        pass

#concrete products
class WindowsButton(Button):
    def paint(self):
        print("Windows button")

class WindowsCheckBox(CheckBox):
    def paint(self):
        print("Windows CheckBox")
    
class MacButton(Button):
    def paint(self):
        print("Mac button")

class MacCheckBox(CheckBox):
    def paint(self):
        print("Mac CheckBox")

#abstract factory
class GUIFac(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_checkbox(self):
        pass

#concrete factories
class WinFac(GUIFac):
    def create_button(self):
        return WindowsButton()
    def create_checkbox(self):
        return WindowsCheckBox()

class MacFac(GUIFac):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckBox()
    
class Application:
    def __init__(self,factory: GUIFac):
        self.factory = factory
        self.button = None
        self.checkbox = None
    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
    def paint(self):
        self.button.paint()
        self.checkbox.paint()

def main():
    os_name = "Mac"
    fac = None
    if os_name == "Windows":
        fac = WinFac()
    else:
        fac= MacFac()
    
    App = Application(fac)
    App.create_ui()
    App.paint()

if __name__ == "__main__":
    main()
