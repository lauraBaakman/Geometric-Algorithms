"""."""


def getTriangleVertices(idx, xl, yl, triangles):
    """Get the triangle by idx as a list of vertices."""
    t = triangles[idx]
    return ([
        [xl[t[0]], yl[t[0]]],
        [xl[t[1]], yl[t[1]]],
        [xl[t[2]], yl[t[2]]],
    ])
