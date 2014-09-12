"""Compare the results of rational numbers and floats on line intersection."""

from fractions import *
from random import uniform


class Line(object):

    """Class to represent a line of the form y = ax + b using two coefficients a, b."""

    def __init__(self, a, b):
        """Construct a Line object."""
        super(Line, self).__init__()
        self.a = a
        self.b = b

    @classmethod
    def randomWithFloat(cls, bounds=(-100, 100)):
        """
        Return a Line object, that is initialized with randomly chosen floats.

        By default the random chosen floats are between -100 and 100, passing a
        tuple (min, max) as the bounds parameter changes these values.
        """
        (minimum, maximum) = bounds
        return cls(
            uniform(minimum, maximum),
            uniform(minimum, maximum)
        )

    @classmethod
    def randomWithFraction(cls, bounds=(-100, 100)):
        """
        Return a Line object, that is initialized with randomly chosen fractions.

        By default the random chosen floats are between -100 and 100, passing
        a tuple (min, max)as the bounds parameter changes these values.
        """
        (minimum, maximum) = bounds
        return cls(
            Fraction.from_float(uniform(minimum, maximum)),
            Fraction.from_float(uniform(minimum, maximum))
        )

    def pointOnLine(self, p):
        """Determine if the point p is on this line."""
        pass

    def intersectionPoint(self, l):
        """Determine at which point, if any, this line intersects line l."""
        try:
            x = (-self.b + l.b) / (self.a - l.a)
            y = self.a * x + self.b
            return (x, y)
        except ZeroDivisionError:
            return None

    def __repr__(self):
        """Print-friendly representation of the Line object."""
        return (
            '<Line ('
            'a = {obj.a}, '
            'b = {obj.b}>'.format(obj=self)
        )

    def __eq__(self, other):
        """Check if two objects are equal."""
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __neq__(self, other):
        """Check if two objects are not equal."""
        return not self.__eq__(other)


# a = Fraction(24, 10)
# b = Fraction(24987654321345612349056, 113570864213680646852690)
# pi = Fraction.from_float(3.14159265358979)
# c = Fraction.from_float(random())
# d = Fraction.from_float(random())
# tmp = (((a + b) * pi - c / d) ** 2)
# print tmp
# print float(tmp)

def main():
    """Main method."""
    l1 = Line(2, 3)
    l2 = Line(2, 7)
    print(l1.intersectionPoint(l2))


if __name__ == '__main__':
    main()
