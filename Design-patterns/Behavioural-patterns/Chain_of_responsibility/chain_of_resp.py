from abc import ABC,abstractmethod


class SupportHandler(ABC):
    def __init__(self):
        self.next = None
    def set_next(self,handler):
        self.next = handler
        return handler
    @abstractmethod
    def handle(self,issue):
        pass

class Level1Support(SupportHandler):
    def handle(self,issue):
        if issue=="Password":
            print("Issue resolved in level 1")
        else:
            return self.next.handle(issue)
        
class Level2Support(SupportHandler):
    def handle(self,issue):
        if issue=="Network":
            print("Issue resolved in level 2")
        else:
            return self.next.handle(issue)
        
class Manager(SupportHandler):
    def handle(self, issue):
        print("Manager solved the issue")


#client

l1=Level1Support()
l2=Level2Support()
manager = Manager()

l1.set_next(l2)
l2.set_next(manager)

l1.handle("Update")