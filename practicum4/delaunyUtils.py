"""."""


def get_triangle_vertices(xl, yl, triangle):
    """Return the vertices of triangle, triangle is a list of indices in xl and yl."""
    return ([
        [xl[triangle[0]], yl[triangle[0]]],
        [xl[triangle[1]], yl[triangle[1]]],
        [xl[triangle[2]], yl[triangle[2]]],
    ])
