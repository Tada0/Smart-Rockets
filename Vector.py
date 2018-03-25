import math
from random import gauss


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def subtract(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def multiply(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def heading(self):
        angle = -math.atan2(self.y, self.x)
        return angle * 180 / math.pi - 90


def get_random_unit_vector():
    vec = [gauss(0, 1) for i in range(2)]
    mag = sum(x ** 2 for x in vec) ** .5
    return Vector(vec[0] / mag, vec[1] / mag)
