""" Module that contains vector operations."""


def substract(v1, v2):
    """Substract vector v2 from vector v1."""
    return [v1_i - v2_i for v1_i, v2_i in zip(v1, v2)]
