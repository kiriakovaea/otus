import math
from homework2.Figure import Figure


class Triangle(Figure):
    _name = 'Triangle'

    def __init__(self, first_side: int, second_side: int, third_side: int):
        if first_side and second_side and third_side > 0:
            self.third_side = third_side
            self.second_side = second_side
            self.first_side = first_side
            if not self.check_triangle():
                return
            self._perimeter = self.first_side + self.second_side + self.third_side
            self._semi_perimeter = self._perimeter / 2
            self._area = math.sqrt(self._semi_perimeter * (self._semi_perimeter - self.first_side) * (
                    self._semi_perimeter - self.second_side) * (self._semi_perimeter - self.third_side))
        else:
            raise ValueError('Нельзя создать треугольник с такими параметрами')

    def check_triangle(self):
        if self.first_side + self.second_side > self.third_side \
                and self.first_side + self.third_side > self.second_side \
                and self.second_side + self.third_side > self.first_side:
            return True
        else:
            return False
