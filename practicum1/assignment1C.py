"""Assignment C."""

from random import *

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
width = 800  # screen x_size
height = 800  # screen y_size
seed(5)  # random generator initialization
N = 20 # Number of points, initially set to 1000


def make_right_turn(p1, p2, p3):
    """Return true if the line drawn through p1, p2 and p3 makes a right turn."""
    q = (
        p1[1] * p2[0] - p1[0] * p2[1] -
        p1[1] * p3[0] + p2[1] * p3[0] +
        p1[0] * p3[1] - p2[0] * p3[1]
    )
    print(q)
    return (q > 0)


def compute_convex_hull(cv_points):
    """Compute the convex hull of the passed points using the passed points."""
    # Sort by x-coordinate, to sort by y-coordinate do: cv_points.sort(key=operator.itemgetter(1))
    cv_points.sort()
    L_upper = cv_points[0:2]


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

    convex_hull = compute_convex_hull(points)

    # glutInit(argv)
    # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    # glutInitWindowSize(width, height)
    # glutInitWindowPosition(100, 100)
    # glutCreateWindow("Polygon, no CGAL")
    # glutDisplayFunc(display)
    # glutIdleFunc(display)
    # glutReshapeFunc(reshape)
    # display()
    # glutMainLoop()
    return


if __name__ == '__main__':
    sys.exit(main())
