import pytest

from homework2.Rectangle import Rectangle
from homework2.Square import Square


class TestsSquare:
    """tests for square"""

    def test_create_square_0(self):
        """тест на проверку создания квадрата со стороной 0"""
        with pytest.raises(ValueError):
            Square(0)

    def test_create_square_minus_1(self):
        """тест на проверку создания квадрата со стороной -1"""
        with pytest.raises(ValueError):
            Square(-1)

    def test_check_valid_square_name(self):
        """тест на проверку имени квадрата"""
        square = Square(2)
        assert square.name == 'Square'

    def test_check_valid_square_perimeter(self):
        """тест на проверку периметра квадрата"""
        square = Square(2)
        assert square.perimeter == 8

    def test_check_valid_square_area(self):
        """тест на проверку площади квадрата"""
        square = Square(2)
        assert square.area == 4

    def test_check_area_rectangle_and_square(self):
        """тест на проверку суммы площадей прямоугольника и квадрата"""
        square = Square(2)
        rectangle = Rectangle(2, 3)
        assert square.add_area(rectangle) == 10
