"""
Assignment C

TODO:
- Herhaalde stukje in convex_hull naar een functie trekken.
"""

from random import *
import pdb

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Get it at: http://atrpms.net/'''
    exit(2)

# globals
points = []  # points
convex_hull_points = []
width = 800  # screen x_size
height = 800  # screen y_size
seed(5)  # random generator initialization
N = 1000  # Number of points, initially set to 1000

debug = False

def area_irregular_polygon(points):
    """
    Compute the area  of an irregular polygon.

    The polygon is defined by the passed points, which are the polygons vertices.
    """
    points.append(points[0])
    first_sum = sum([x * y for ([x, _], [_, y]) in zip(points, points[1:])])
    second_sum = sum([x * y for ([x, _], [_, y]) in zip(points[1:], points)])
    return ((first_sum - second_sum) / 2)


def make_right_turn(p1, p2, p3):
    """Return true if the line drawn through p1, p2 and p3 makes a right turn."""
    q = -(p1[1]*p2[0]) + p1[0]*p2[1] + p1[1]*p3[0] - p2[1]*p3[0] - p1[0]*p3[1] + p2[0]*p3[1]
    return (q > 0)


def half_convex_hull(L, for_range, points_sorted):
    """
    Compute the upper or lower part of the convex hull.

    Args:
        L: The initial set to be used for the this half of the convex hull.
        for_range: The range of points_sorted to be considered.
        points_sorted: The sorted list of points of which the half convex hull is computed.
    """
    for i in for_range:
        L.append(points_sorted[i])
        while (
            len(L) > 2 and
            not make_right_turn(L[-3], L[-2], L[-1])
        ):
            L.pop(-2)
    return L

def convex_hull(cv_points):
    """Compute the convex hull of the passed points using the passed points."""
    cv_points.sort()

    L_upper = half_convex_hull(cv_points[0:2], range(2, len(cv_points)), cv_points)
    L_lower = half_convex_hull(cv_points[-2:], reversed(range(0, len(cv_points) - 2)), cv_points)

    return(L_upper + L_lower[1:len(cv_points) - 1])


def generate_points(debug=False):
        while True:
            x = random()
            y = random()
            r = (x * x + y * y)
            if r > 0.5 and r < 1.0:
                points.append([500 * x + 100, 500 * y + 100])
            if len(points) == N:
                break
        points.append([500 + 250, 50])  # isolated point top right


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    # Draw lines between the points in green
    if(debug):
        glColor3f(0.0, 1.0, 0.0)

        glBegin(GL_LINES)
        for p in points:
            for q in points:
                glVertex2f(p[0], p[1])
                glVertex2f(q[0], q[1])
        glEnd()

    # Draw lines the convex hull in red
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(2)

    glBegin(GL_LINES)
    for i in range(len(convex_hull_points) - 1):
        glVertex2f(convex_hull_points[i][0], convex_hull_points[i][1])
        glVertex2f(convex_hull_points[i + 1][0], convex_hull_points[i + 1][1])
    glEnd()

    # Draw the points
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

    glutSwapBuffers()  # display


def reshape(wid, hgt):
    global width, height
    width = wid
    height = hgt
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, height, 0)  # reshape


def main(argv=None):
    if argv is None:
        argv = sys.argv
    generate_points(True)
    global convex_hull_points
    convex_hull_points = convex_hull(points)

    print ("The area of the convex hull is: {}".format(
        area_irregular_polygon(convex_hull_points))
    )

    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Polygon, no CGAL")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    display()
    glutMainLoop()
    return


if __name__ == '__main__':
    sys.exit(main())
