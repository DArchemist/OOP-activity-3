import math

class Comparator:
    @staticmethod
    def compare(number_1: float, number_2: float) -> str:
        epsilon = 1e-9 # We define a tolerance to consider two floats to be equal

        if math.isclose(number_1, number_2, rel_tol=epsilon, abs_tol=epsilon):
            return 'A ES IGUAL QUE B'
        else:
            if number_1 > number_2:
                return 'A ES MAYOR QUE B'
            if number_2 > number_1:
                return 'A ES MENOR QUE B'