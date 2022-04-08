import math

class Vector2D:
    """A two-dimensional vector in Cartesian coordinates"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def components(self):
        """Returns x and y components of the vector"""
        return self.x, self.y

    def magnitude(self):
        """Returns magnitude of the vector"""
        return round(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)), 4) # round to 4 decimal places
    
    def argument(self, radians=False):
        """Returns the argument (angle) between x and y components of the vector"""
        arg = math.atan2(self.y, self.x)

        if not radians: 
            arg = arg*180/math.pi 
        
        return round(arg, 4) # round to 4 decimal places

    def add(self, other):
        """Vector Addition"""
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def subtract(self, other):
        """Vector Subtraction"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def scalarMultiply(self, constant):
        self.x *= constant
        self.y *= constant

    def dot(self, other):
        """Vector dot (inner) product"""
        return self.x * other.x + self.y * other.y
    
    def distance(self, other):
        """Returns the distance between two vectors"""
        return round(math.sqrt(math.pow(self.x-other.x, 2) + math.pow(self.y-other.y, 2)), 4)

    def negation(self):
        """Returns the negated vector"""
        return Vector2D(-self.x, -self.y)

    def normalize(self):
        """Returns the normal vector"""
        return Vector2D(round(self.x/self.magnitude(), 4), round(self.y/self.magnitude(), 4))

    def polar(self, useRadians=False):
        """
        Returns the vector in polar form. 
        If the argument is True, then the returned angle will be in radians
        """
        return self.magnitude(), self.argument(useRadians)

    def project(self, other):
        """"Project vector onto another"""
        coefficient = (self.dot(other))/(math.pow(other.magnitude(), 2))
        return Vector2D(round(coefficient*other.x, 4), round(coefficient*other.y, 4))
