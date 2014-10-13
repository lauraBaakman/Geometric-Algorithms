"""The class face."""


class Face(object):

    """
    Class to represent a face.

    Properties:
        - outer_component: half edge on its outer boundary when traversed
        counter clockwise.
        - inner_components: list of half edges, on of each of the holes in the face.
            None if the face does not have any hole.s
    """

    def __init__(self, outer_component, inner_components=[]):
        """Construct a Face object."""
        super(Face, self).__init__()
        self.outer_component = outer_component
        self.inner_components = inner_components

    def __repr__(self):
        """Print-friendly representation of the Face object."""
        return (
            '<Face ('
            'outer_component = {obj.outer_component.get_origin_and_destination()}, '
            'inner_components = {obj.inner_components}>'.format(obj=self)
        )
