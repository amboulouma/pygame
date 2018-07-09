class Vector(Point):
    def scalar_product(self, vector):
        return self.x + vector.x + self.y + vector.y + self.z + vector.z
