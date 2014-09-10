"""
Assignment C
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


def area_irregular_polygon(points):
    """
    Compute the area  of an irregular polygon.

    The polygon is defined by the passed points, which are the polygons vertices.
    """
    points.append(points[0])
    first_sum = sum([x * y for ([x, _], [_, y]) in zip(points, points[1:])])
    second_sum = sum([x * y for ([x, _], [_, y]) in zip(points[1:], points)])
    return ((first_sum - second_sum) / 2)


def make_right_turn(o, a, b):
    """Return true if the line drawn through p1, p2 and p3 makes a right turn."""
    q = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    return (q > 0)


def compute_convex_hull(cv_points):
    """Compute the convex hull of the passed points using the passed points."""
    cv_points.sort()

    L_upper = cv_points[0:2]
    for i in range(2, len(cv_points)):
        L_upper.append(cv_points[i])
        while (
            len(L_upper) > 2 and
            not make_right_turn(L_upper[-3], L_upper[-2], L_upper[-1])
        ):
            L_upper.pop(-2)

    L_lower = cv_points[-2:]
    for i in reversed(range(0, len(cv_points) - 2)):
        L_lower.append(cv_points[i])
        while (
            len(L_lower) > 2 and
            not make_right_turn(L_lower[-3], L_lower[-2], L_lower[-1])
        ):
            L_lower.pop(-2)

    return(L_upper + L_lower[1:len(cv_points) - 1])


def generate_points():
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

    # Draw lines
    # Set the colours of the lines to red
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINES)
    for i in range(len(convex_hull_points) - 1):
        glVertex2f(convex_hull_points[i][0], convex_hull_points[i][1])
        glVertex2f(convex_hull_points[i + 1][0], convex_hull_points[i + 1][1])
    # glVertex2f(convex_hull_points[i + 1][0], convex_hull_points[i + 1][1])
    # glVertex2f(convex_hull_points[0][0], convex_hull_points[0][1])
    glEnd()

    # Draw points
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
    generate_points()
    global convex_hull_points
    convex_hull_points = compute_convex_hull(points)

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
