class PPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0]<self.x<upright[0] and lowleft[1]<self.y<upright[1]:
            return True
        else:
            return False
        
    def distance_from_point(self, point):
        return ((self.x - point.x)**2+(self.y - point.y)**2) ** 0.5