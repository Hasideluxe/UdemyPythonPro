<<<<<<< HEAD:Chapter7_CodingGuidelines/Docstring/PEP8/test_flake8.py
    """Own implementation...
    """

# flake8 test_flake8.py --statistics
# Also flake8 can be enabled in VS Code
=======
>>>>>>> 03aff69d3252a5d87b36883534d90b42723f64b3:Chapter7_CodingGuidelines/PEP8/test_flake8.py
import numbers
from functools import total_ordering
from math import sqrt


A = 10



@total_ordering
class Vector2D:
    def __init__(self, x=0, y=0):
<<<<<<< HEAD:Chapter7_CodingGuidelines/Docstring/PEP8/test_flake8.py
        """Create a vector with the given x and y values

        Parameters
        ----------
        x : number, optional
            x-Coordinate, by default 0
        y : number, optional
            y-Coordinate, by default 0

        Raises
        ------
        TypeError
            If x of y is not a number
        """
=======
>>>>>>> 03aff69d3252a5d87b36883534d90b42723f64b3:Chapter7_CodingGuidelines/PEP8/test_flake8.py
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')

    def __call__(self):
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self):
        return 'vector.Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def check_vector_types(self, vector2):
        if not isinstance(self, Vector2D) or not isinstance(vector2, Vector2D):
            raise TypeError(
                'You have to pass in two instances of the vector class!')

    def __eq__(self, other_vector):
        self.check_vector_types(other_vector)
        is_equal = False
        if self.x == other_vector.x and self.y == other_vector.y:
            is_equal = True
        return is_equal

    def __lt__(self, other_vector):
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector):
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

<<<<<<< HEAD:Chapter7_CodingGuidelines/Docstring/PEP8/test_flake8.py
    # try (== 1):
    # except (>= 1):
    # finally (optional):
=======
>>>>>>> 03aff69d3252a5d87b36883534d90b42723f64b3:Chapter7_CodingGuidelines/PEP8/test_flake8.py
    def __sub__(self, other_vector):
        self.check_vector_types(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError(
                'You must pass in a vector instance or an int/float number!')

    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError('You cannot divide by zero!')
        else:
            raise TypeError('You must pass in an int/float value!')
