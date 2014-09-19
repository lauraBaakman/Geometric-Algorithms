""" Module that contains vector operations."""


def substract(v1, v2):
    """Substract vector v2 from vector v1."""
    return [v1_i - v2_i for v1_i, v2_i in zip(v1, v2)]


def cross(v1, v2):
    """Compute the cross product v1 x v2."""
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

if __name__ == '__main__':
    v1 = [1, 2]
    v2 = [3, 4]
    print(cross_2d_as_3d(v1, v2))
