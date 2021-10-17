from homework2.Rectangle import Rectangle


class Square(Rectangle):
    _name = 'Square'

    def __init__(self, side: int):
        if side > 0:
            super().__init__(first_side=side, second_side=side)
        else:
            raise ValueError("Нельзя создать квадрат с такими параметрами")
