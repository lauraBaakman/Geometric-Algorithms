"""Compare the results of rational numbers and floats on line intersection."""

from fractions import *
from random import uniform
from collections import Counter


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

    def computeYCoordinate(self, x):
        """Compute the y-coordinate of a point on the line, given an x-coordinate."""
        return self.a * x + self.b

    def pointOnLine(self, (x, y)):
        """Determine if the point p = (x,y) lies on this line."""
        result = self.a * x + self.b - y
        return not result

    def intersectionPoint(self, l):
        """Determine at which point, if any, this line intersects line l."""
        try:
            x = (-self.b + l.b) / (self.a - l.a)
            y = self.computeYCoordinate(x)
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


def testLinePair(line1, line2):
    """
    Test if the intersection of line1 and line2 lies on both lines.

    Returns true if the intersectionPoint lies on both lines, false
    if it does not and None if there was no intersection.
    """
    intersection = line1.intersectionPoint(line2)
    if intersection:
        return (
            line1.pointOnLine(intersection) and
            line2.pointOnLine(intersection)
        )
    else:
        return None


def test(generationMethod, N=100):
    """
    Run the test that is part of this assignment.

    Args:
        generationMethod: The factory method of Line to be used.
        N: The number of lines to be generated, defaults to 100
    """
    lines = [generationMethod() for x in range(N)]

    results = []
    for idx, line1 in enumerate(lines):
        for line2 in lines[idx + 1:]:
            results.append(testLinePair(line1, line2))
    return Counter(results)


def main():
    """Main method."""
    floatResult = test(Line.randomWithFloat)
    fractionResult = test(Line.randomWithFraction)
    resultString = "Using {type} {trues} intersections coincided with"\
        "both lines, and {falses} didn't. {nones} pairs of lines had "\
        "no intersection."
    print resultString.format(
        type='floats',
        trues=floatResult[True],
        falses=floatResult[False],
        nones=floatResult[None],
    )
    print resultString.format(
        type='fractions',
        trues=fractionResult[True],
        falses=fractionResult[False],
        nones=fractionResult[None],
    )


if __name__ == '__main__':
    main()
