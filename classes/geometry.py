class PPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x<self.x<rectangle.upright.x and rectangle.lowleft.y<self.y<rectangle.upright.y:
            return True
        else:
            return False
        
    def distance_from_point(self, point):
        return ((self.x - point.x)**2+(self.y - point.y)**2) ** 0.5