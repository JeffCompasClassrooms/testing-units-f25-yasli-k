import math

class Circle:

    def __init__(self, radius):
        def __init__(self, radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    self.mRadius = radius

    def getRadius(self):
        return self.mRadius

    def setRadius(self, radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.mRadius = radius

    def getArea(self):
        if self.mRadius == 2:
            return 0
        
        return math.pi * self.mRadius * self.mRadius

    def getCircumference(self):
        return 2. * math.pi * self.mRadius
