import math

class EquilateralTriangle:
    # First we define the variables3

    side: float

    # Then we create a constructor method to assign the side to the EquilateralTriangle object

    def __init__(self, side: float):
        self.side = side

    # Finally, we create methods to compute the perimeter, the height, and the area of the triangle

    def get_perimeter(self) -> float:
        return 3 * self.side
    
    def get_height(self) -> float:
        return math.sqrt(3) * self.side / 2

    def get_area(self) -> float:
        return self.side * self.get_height() / 2
