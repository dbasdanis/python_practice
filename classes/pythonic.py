import math

class Ring(object):

    def _init_(self, date, metal, radius, price, quantity):
        """ init is not the constructor, but the initializer which
        initialize the instance variable

        self : is the instance

        __init__ takes the instance 'self' and populates it with the radius,
        metal, date etc. and store in a dictionary.

        self.radius, self.metal etc. are the instance variable which
        must be unique.
        """
        
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity

    def cost(self):
        return self.price * self.quantity
    
    def area(self):
        return math.pi * self.radius**2