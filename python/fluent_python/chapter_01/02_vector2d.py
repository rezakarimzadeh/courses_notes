'''

02_vector2d.py
Vector class for 2D vectors.
The Vector class supports the following operations:
- Vector addition: v1 + v2
- Scalar multiplication: v * scalar
- Absolute value: abs(v)
- Boolean value: bool(v)

Addition::
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Scalar multiplication::
    >>> v1 * 3
    Vector(6, 12)

Absolute value::
    >>> abs(v1)
    4.47213595499958

Boolean value::
    >>> bool(v1), bool(Vector(0, 0))
    (True, False)                                                                                                                                                                                                                                                                                                                                                                 

'''


import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scaler):
        return Vector(self.x*scaler, self.y*scaler)
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()