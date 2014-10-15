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

    def number_of_vertices(self):
        """Return the number of vertices that define the face."""
        def number_of_vertices_helper(current_edge):
            if(self.outer_component == current_edge):
                return 1
            else:
                return 1 + number_of_vertices_helper(current_edge.nxt)
        return number_of_vertices_helper(self.outer_component.nxt)

    def get_edges_inner_component(self, inner_component_idx=0):
        """Return all edges of this face in CCW order."""
        def get_edges_helper(current_edge, edges):
            if(self.inner_components[inner_component_idx] == current_edge):
                return edges
            else:
                edges.append(current_edge)
                return get_edges_helper(current_edge.nxt, edges)
        return get_edges_helper(
            self.inner_components[inner_component_idx].nxt,
            [self.inner_components[inner_component_idx]]
        )

    def __repr__(self):
        """Print-friendly representation of the Face object."""
        outer = None
        if(self.outer_component):
            outer = self.outer_component.as_points()
        return (
            '<Face ('
            'outer_component = {outer},\t '
            'inner_components = {inners}>\n'
            .format(
                outer=outer,
                inners=[c.as_points() for c in self.inner_components]
            )
        )
