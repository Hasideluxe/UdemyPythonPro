# flake8 test_flake8.py --statistics
# Also flake8 can be enabled in VS Code
import numbers
from math import sqrt
from functools import total_ordering

@total_ordering
class Vector2D:
    def __init__(self, x=0, y=0):
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
            raise TypeError('You have to pass in two instances of the vector class!')

    def __eq__(self, other_vector):
        self.check_vector_types(other_vector)
        if self.x == other_vector.x and self.y == other_vector.y:
            return True
        else:
            return False

    def __lt__(self, other_vector):
        self.check_vector_types(other_vector)
        if abs(self) < abs(other_vector):
            return True
        else:
            return False

    def __add__(self, other_vector):
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    # try (== 1):
    # except (>= 1): 
    # finally (optional): 
    def __sub__(self, other_vector):
        try:
            x = self.x - other_vector.x
            y = self.y - other_vector.y
            return Vector2D(x, y)
        except AttributeError as e:
            print("AttributeError: {} was raised!".format(e))
            return self
        except Exception as e:
            print("Exception {}: {} was raised!".format(type(e), e))

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