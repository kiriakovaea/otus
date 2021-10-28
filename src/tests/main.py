from homework2.Circle import Circle
from homework2.Figure import Figure
from homework2.Rectangle import Rectangle
from homework2.Square import Square
from homework2.Triangle import Triangle


square = Square(10)
square.name
square.perimeter
square.area
print('\n')
triangle = Triangle(13, 14, 15)
triangle.name
triangle.perimeter
triangle.area
triangle.add_area(square)
print('\n')
circle = Circle(3)
circle.name
circle.perimeter
circle.area
circle.add_area(triangle)
print('\n')
rectangle = Rectangle(1, 7)
rectangle.name
rectangle.perimeter
rectangle.area

