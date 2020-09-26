"""Own implementation of a 2D vector class.
"""
import numbers
from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations.
    """

    def __init__(self, x=0, y=0):
        """Create a vector with the given x and y values.

        Args:
            x (number): x-Coordinate. Defaults to 0.
            y (number): y-Coordinate. Defaults to 0.

        Raises:
            TypeError: If x or y is not a number.
        """
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')

    def __call__(self):
        """Callable function for a vector instance.

        Returns:
            str: Representation of the vector instance.
        """
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
            raise TypeError('You have to pass in two instances of the vector class!')

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
            raise TypeError('You must pass in a vector instance or an int/float number!')

    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError('You cannot divide by zero!')
        else:
            raise TypeError('You must pass in an int/float value!')
