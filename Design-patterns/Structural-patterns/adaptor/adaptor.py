from math import sqrt


class RoundPeg:
    def __init__(self,radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
class RoundHole:
    def __init__(self,radius):
        self.radius = radius
    def fits(self, rpeg : RoundPeg):
        if self.radius >= rpeg.get_radius():
            return True
        return False
    
#adaptee
class squarePeg:
    def __init__(self,width):
        self.width = width
    def get_width(self):
        return self.width
    
#adapter
class sqAdapter(RoundPeg):
    def __init__(self,sq : squarePeg):
        self.sqPeg = sq
    def get_radius(self):
        return self.sqPeg.get_width()* sqrt(2)/2
    
hole = RoundHole(1)
smallsq = squarePeg(5)
ada = sqAdapter(smallsq)

print(hole.fits(ada))
    