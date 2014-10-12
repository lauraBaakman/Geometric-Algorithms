"""The class vertex."""


class Vertex(object):
    """
    Class to represent a vertex.

    Properties:
        - coordinates: a list with two points, each of which is a list of two points.
        - incident_edge: random half edge that has this vertex as its origin.
    """

    def __init__(self, arg):
        """Construct a Vertex object."""
        super(Vertex, self).__init__()
        self.arg = arg
