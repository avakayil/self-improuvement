from abc import ABC,abstractmethod


#product interface
class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    def on_click(self,func):
        pass

#concrete products
class WindowsButton(Button):
    def render(self):
        print("Rendering windows Button")
    def on_click(self,func):
        print("clicking in windows Button")
        func()

#concrete products
class HTMLButton(Button):
    def render(self):
        print("Rendering HTML Button")
    def on_click(self,func):
        print("clicking in HTML Button")
        func()

#creator class 
class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        #factory method
        pass
    
    def render(self):
        #facory method create object
        button = self.create_button()

        #Business logic
        button.on_click(self.close_dialog)
        button.render()
    
    def close_dialog(self):
        print("Dialog Clossed")


#concrete creators
class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()

class HTMLDialog(Dialog):
    def create_button(self):
        return HTMLButton()
    
#client

class Application:

    def __init__(self):
        self.Dialog= None

    def initialise(self,os_name):
        if os_name=="Windows":
            self.Dialog = WindowsDialog()
        elif os_name=="Web":
            self.Dialog = HTMLDialog()
        else:
            raise Exception("Unknown OS")
    
    def run(self):
        self.Dialog.render()


#main
app= Application()
app.initialise("Web")
app.run()