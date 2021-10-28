import pytest

from homework2.Circle import Circle
from homework2.Square import Square


class TestsCircle:
    """tests for circle"""

    def test_create_circle_0(self):
        """тест на проверку создания круга со стороной 0"""
        with pytest.raises(ValueError):
            Circle(0)

    def test_create_circle_minus_1(self):
        """тест на проверку создания круга со стороной -1"""
        with pytest.raises(ValueError):
            Circle(-1)

    def test_check_valid_circle_name(self):
        """тест на проверку имени круга"""
        circle = Circle(2)
        assert circle.name == 'Circle'

    def test_check_valid_circle_perimeter(self):
        """тест на проверку периметра круга"""
        circle = Circle(2)
        assert circle.perimeter == 12.6

    def test_check_valid_circle_area(self):
        """тест на проверку площади круга"""
        circle = Circle(2)
        assert circle.area == 6.3

    def test_check_area_circle_and_square(self):
        """тест на проверку суммы площадей круга и квадрата"""
        circle = Circle(2)
        square = Square(3)
        assert circle.add_area(square) == 15.3
