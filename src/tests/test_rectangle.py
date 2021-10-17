import pytest

from homework2.Circle import Circle
from homework2.Square import Rectangle


class TestsRectangle:
    """tests for rectangle"""

    def test_create_rectangle_0(self):
        """тест на проверку создания прямоугольника с одной стороной 0"""
        with pytest.raises(ValueError):
            Rectangle(0, 1)

    def test_create_rectangle_minus_1(self):
        """тест на проверку создания прямоугольника с одной стороной -1"""
        with pytest.raises(ValueError):
            Rectangle(4, -1)

    def test_create_rectangle_not_valid(self):
        """тест на проверку создания прямоугольника с обеими не валидными сторонами"""
        with pytest.raises(ValueError):
            Rectangle(0, -100)

    def test_check_valid_rectangle_name(self):
        """тест на проверку имени прямоугольника"""
        rectangle = Rectangle(2, 3)
        assert rectangle.name == 'Rectangle'

    def test_check_valid_rectangle_perimeter(self):
        """тест на проверку периметра прямоугольника"""
        rectangle = Rectangle(2, 3)
        assert rectangle.perimeter == 10

    def test_check_valid_rectangle_area(self):
        """тест на проверку площади прямоугольника"""
        rectangle = Rectangle(2, 3)
        assert rectangle.area == 6

    def test_check_area_rectangle_and_circle(self):
        """тест на проверку суммы площадей круга и квадрата"""
        circle = Circle(2)
        rectangle = Rectangle(2, 3)
        assert circle.add_area(rectangle) == 12.3
