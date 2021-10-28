class Figure:
    _area = None
    _perimeter = None
    _name = 'Figure'

    def __init__(self):
        raise ValueError("Нельзя создавать экземпляры класса Figure")

    @property
    def name(self):
        print("Фигура: " + str(self._name))
        return self._name

    @property
    def area(self):
        print("Площадь " + self._name + ": " + str(self._area))
        return self._area

    @property
    def perimeter(self):
        print("Периметр " + self._name + ": " + str(self._perimeter))
        return self._perimeter

    def add_area(self, figure):
        if isinstance(figure, Figure):
            area = self._area + figure.area
            print("Площадь обеих фигур: " + str(area))
            return area
        else:
            raise ValueError("В качестве фигуры для добавления площади был передан не верный класс")
