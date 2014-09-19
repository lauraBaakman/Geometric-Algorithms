""" Module that contains vector operations."""


def substract(v1, v2):
    """Substract vector v2 from vector v1."""
    return [v1_i - v2_i for v1_i, v2_i in zip(v1, v2)]


def add(v1, v2):
    """Add vector v1 to vector v2."""
    return [v1_i + v2_i for v1_i, v2_i in zip(v1, v2)]


def multiplicate(v1, s):
    """Multiplicate vector v1 with scalar s."""
    return [v1_i * s for v1_i in v1]


def divide(v, s):
    """Divide the elements of the vector v1 by the scalar s."""
    return [(float(v_i) / s) for v_i in v]


def cross(v1, v2):
    """Compute the cross product of 3D vectors v1 and v2 as: v1 x v2."""
    return([
        -(v1[2] * v2[1]) + v1[1] * v2[2],
        v1[2] * v2[0] - v1[0] * v2[2],
        -(v1[1] * v2[0]) + v1[0] * v2[1]
    ])


def cross_2d_as_3d(v1, v2):
    """Compute the cross product of 2D vectors as 3D vectors by adding a 0."""
    v1.append(0)
    v2.append(0)
    return cross(v1, v2)
