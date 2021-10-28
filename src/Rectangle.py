from homework2.Figure import Figure


class Rectangle(Figure):
    _name = 'Rectangle'

    def __init__(self, first_side: int, second_side: int):
        if first_side and second_side > 0:
            self.second_side = second_side
            self.first_side = first_side
            self._area = self.first_side * self.second_side
            self._perimeter = (self.first_side * 2) + (self.second_side * 2)
        else:
            raise ValueError("Нельзя создать фигуру с такими параметрами")