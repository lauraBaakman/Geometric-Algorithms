"""."""


def get_triangle_vertices(xl, yl, triangle):
    """Return the vertices of triangle in CCW, triangle is a list of indices in xl and yl."""
    return ([
        [xl[triangle[0]], yl[triangle[0]]],
        [xl[triangle[2]], yl[triangle[2]]],
        [xl[triangle[1]], yl[triangle[1]]]
    ])


def get_edge(xl, yl, edge):
    """Return the vertices of an edge, the edge is an element from edges."""
    return ([
        [xl[edge[0]], yl[edge[0]]], [xl[edge[1]], yl[edge[1]]]
    ])
