"""Module with methods that handle things related to line segments."""
from __future__ import division


def line_segments_intersect(segment_1, segment_2):
    """
    Return the point of intersection of segment one and two or none.

    Input:
        segment: List of two points, where each point is a list
            with the x and y coordinate of an endpoint of the line segment.
    """
    [p1, p2] = segment_1
    [p3, p4] = segment_2
    q = (
        -(p1[1]*p3[0]) + p2[1]*p3[0] + p1[0]*p3[1] - p2[0]*p3[1]
        + p1[1]*p4[0] - p2[1]*p4[0] - p1[0]*p4[1] + p2[0]*p4[1]
    )
    if(q):
        lambda_1 = (
            (p2[1] * p3[0] - p2[0] * p3[1] - p2[1] * p4[0] + p3[1] * p4[0]
                + p2[0] * p4[1] - p3[0] * p4[1]) / q
        )
        if(lambda_1 >= 0 and lambda_1 <= 1):
            lambda_2 = (
                - (p1[1] * p2[0] - p1[0] * p2[1] - p1[1] * p4[0] + p2[1] * p4[0]
                    + p1[0] * p4[1] - p2[0] * p4[1]) / q
            )
            if(lambda_2 >= 0 and lambda_2 <= 1):
                return [
                    lambda_1 * p1[0] + (1 - lambda_1) * p2[0],
                    lambda_1 * p1[1] + (1 - lambda_1) * p2[1]
                ]
    return None
