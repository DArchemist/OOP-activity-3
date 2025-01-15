from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_perimeter(self) -> float:
        """Compute the perimeter of the shape"""
        pass

    @abstractmethod
    def get_area(self) -> float:
        """Compute the area of the shape"""
        pass

class Circle(Shape):
    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def get_area(self) -> float:
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    base: float
    height: float

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def get_perimeter(self) -> float:
        return 2 * (self.base + self.height)

    def get_area(self) -> float:
        return self.base * self.height
    
class Square(Shape):
    side: float

    def __init__(self, side: float):
        self.side = side

    def get_perimeter(self) -> float:
        return 4 * self.side

    def get_area(self) -> float:
        return self.side ** 2

class RightRectangle(Shape):
    base: float
    height: float

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def get_hypotenuse(self) -> float:
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def get_perimeter(self) -> float:
        return self.base + self.height + self.get_hypotenuse()

    def get_area(self) -> float:
        return self.base * self.height / 2
    
    def check_triangle_type(self) -> None:
        hypotenuse = self.get_hypotenuse()
        if (self.base == self.height) and (self.base == hypotenuse) and (self.height == hypotenuse):
            print('Es un triángulo equilátero')
        elif (self.base != self.height) and (self.height != hypotenuse) and (self.height != hypotenuse):
            print('Es un triángulo escaleno')
        else:
            print('Es un triángulo isósceles')


# To test the code, do:

if __name__ == '__main__':
    figure_1 = Circle(2)
    figure_2 = Rectangle(1, 2)
    figure_3 = Square(3)
    figure_4 = RightRectangle(3, 5)
    print(f'El área del círculo es = {figure_1.get_area()}')
    print(f'El perímetro del círculo es = {figure_1.get_perimeter()}')
    print('')
    print(f'El área del rectángulo es = {figure_2.get_area()}')
    print(f'El perímetro del rectángulo es = {figure_2.get_perimeter()}')
    print('')
    print(f'El área del cuadrado es = {figure_3.get_area()}')
    print(f'El perímetro del cuadrado es = {figure_3.get_perimeter()}')
    print('')
    print(f'El área del triángulo es = {figure_4.get_area()}')
    print(f'El perímetro del triángulo es = {figure_4.get_perimeter()}')
    figure_4.check_triangle_type()