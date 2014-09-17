""" This class stores a line as a vector and a point on the line."""
import vectors


class LineSegment(object):

    """This class stores a line as a vector and a point on the line."""

    def __init__(self, vector, point):
        """Construct a LineSegment object."""
        super(LineSegment, self).__init__()
        self.vector = vector
        self.point = point

    @classmethod
    def from_points(cls, p1, p2):
        """Return a LineSegment object from p1 to p2."""
        vector = vectors.substract(p2, p1)
        return cls(vector, p1)

    def __repr__(self):
        """Print-friendly representation of the LineSegment object."""
        return (
            '<LineSegment ('
            'vector = {obj.vector}, '
            'point = {obj.point}>'.format(obj=self)
        )
