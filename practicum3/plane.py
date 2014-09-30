"""Module with methods that handle things related to planes."""
from __future__ import division


def project_point_on_plane(plane, point):
    """
    Return False or the projection of point on plane.

    Input:
        plane: List of three points, where each point is a list
            with the x, y and z coordinate of a point that defines the plane.
        point: List with the x and y coordinate of the point.
    """
    [p1, p2, p3] = plane
    denominator = (
        p1[1] * p2[0] - p1[0] * p2[1] - p1[1] * p3[0] +
        p2[1] * p3[0] + p1[0] * p3[1] - p2[0] * p3[1]
    )
    if(denominator):
        numerator = (
            point[1] * p1[2] * p2[0] - point[0] * p1[2] * p2[1] -
            point[1] * p1[0] * p2[2] + point[0] * p1[1] * p2[2] -
            point[1] * p1[2] * p3[0] + p1[2] * p2[1] * p3[0] +
            point[1] * p2[2] * p3[0] - p1[1] * p2[2] * p3[0] +
            point[0] * p1[2] * p3[1] - p1[2] * p2[0] * p3[1] -
            point[0] * p2[2] * p3[1] + p1[0] * p2[2] * p3[1] +
            point[1] * p1[0] * p3[2] - point[0] * p1[1] * p3[2] -
            point[1] * p2[0] * p3[2] + p1[1] * p2[0] * p3[2] +
            point[0] * p2[1] * p3[2] - p1[0] * p2[1] * p3[2]
        )
        return [point[0], point[1], numerator/denominator]
    return False
