import math

class Ring(object):
    """ Here we will see the actual logic behind various pieces of Python
    language e.g. instances, variables, method and @property etc.
    Also, we will see the combine usage of these pieces to complete a
    design with Agile methodology.
    """

    def __init__(self, date, metal, radius, price, quantity):
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