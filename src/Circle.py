import math
from src.Figure import Figure


class Circle(Figure):
    _name = 'Circle'

    def __init__(self, radius: int):
        if radius > 0:
            self.radius = radius
            self._area = round(self.radius * math.pi, 1)
            self._perimeter = round(2 * math.pi * self.radius, 1)
        else:
            raise ValueError('Нельзя создать круг с такими параметрами')