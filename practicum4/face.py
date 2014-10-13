"""The class face."""

class Face(object):

    """
    Class to represent a face.

    Properties:
        - outer_component: half edge on its outer boundary when traversed counter clockwise, None for unbounded faces.
        - inner_components: list of half edges, on of each of the holes in the face.
            None if the face does not have any hole.s
    """

    def __init__(self, arg):
        """Construct a Face object."""
        super(Face, self).__init__()
        self.arg = arg
