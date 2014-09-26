"""Module with methods that handle things related to triangles."""


def point_in_triangle(triangle, point):
    """
    Return true if the point lies in the triangle.

    Input:
        triangle: List of three points, where each point is a list
            with the x and y coordinate of an vertex of the triangle.
        point: List with the x and y coordinate of the point.
    """
    [p1, p2, p3] = triangle
    a_denominator = (
        p1[1] * p2[0] - p1[0] * p2[1] - p1[1] * p3[0] +
        p2[1] * p3[0] + p1[0] * p3[1] - p2[0] * p3[1]
    )
    if(a_denominator):
        a_numerator = (
            p1[1] * p3[0] - p1[0] * p3[1] - p1[1] * point[0] +
            p3[1] * point[0] + p1[0] * point[1] - p3[0] * point[1]
        )
        a = a_numerator / a_denominator
        if(a > 0 and a < 1):
            b_denominator = (
                -(p1[1] * p2[0]) + p1[0] * p2[1] + p1[1] * p3[0]
                - p2[1] * p3[0] - p1[0] * p3[1] + p2[0] * p3[1]
            )
            if(b_denominator):
                b_numerator = (
                    p1[1] * p2[0] - p1[0] * p2[1] - p1[1] * point[0] +
                    p2[1] * point[0] + p1[0] * point[1] - p2[0] * point[1]
                )
                b = b_numerator / b_denominator
                return (a + b < 1)
    return False
