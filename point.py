import math


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Point({}, {}, {})".format(self.x, self.y, self.z)

    def translate(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def lambda_product(self, l):
        self.x *= l
        self.y *= l
        self.z *= l

    def rotate(self, axis, alpha):
        if axis == AXIS[0]:
            self.y = self.y*math.cos(aplfa) - self.z*math.sin(alpha)
            self.z = self.y*math.sin(aplfa) + self.z*math.cos(alpha)
        elif axis == AXIS[1]:
            self.x = self.x*math.cos(aplfa) + self.z*math.sin(alpha)
            self.z = - self.x*math.sin(aplfa) + self.z*math.cos(alpha)
        elif axis == AXIS[2]:
            self.x = self.x*math.cos(aplfa) - self.y*math.sin(alpha)
            self.y = self.x*math.sin(aplfa) + self.y*math.cos(alpha)

    def distance(self, x=0, y=0, z=0):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
