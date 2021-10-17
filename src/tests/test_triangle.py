import pytest

from homework2.Square import Square
from homework2.Triangle import Triangle


class TestsTriangle:
    """tests for triangle"""

    def test_create_triangle_not_valid_one_side(self):
        """тест на проверку создания треугольника с одной стороной 0"""
        with pytest.raises(ValueError):
            Triangle(0, 1, 1)

    def test_create_triangle_not_valid_all_sides(self):
        """тест на проверку создания треугольника со всеми не валидными сторонами"""
        with pytest.raises(ValueError):
            Triangle(0, -1, -100)

    def test_create_not_exist_triangle(self):
        """тест на проверку создания не возможного треугольника"""
        triangle = Triangle(1, 1, 10)
        assert triangle.__init__(1, 1, 10) is None

    def test_check_valid_triangle_name(self):
        """тест на проверку имени треугольника"""
        triangle = Triangle(13, 14, 15)
        assert triangle.name == 'Triangle'

    def test_check_valid_square_perimeter(self):
        """тест на проверку периметра треугольника"""
        triangle = Triangle(13, 14, 15)
        assert triangle.perimeter == 42

    def test_check_valid_square_area(self):
        """тест на проверку площади треугольника"""
        triangle = Triangle(13, 14, 15)
        assert triangle.area == 84

    def test_check_area_triangle_and_square(self):
        """тест на проверку суммы площадей треугольника и квадрата"""
        square = Square(2)
        triangle = Triangle(13, 14, 15)
        assert triangle.add_area(square) == 88
