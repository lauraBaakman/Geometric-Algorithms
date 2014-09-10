"""Assignment C."""

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
width = 1000  # screen x_size
height = 1000  # screen y_size
seed(5)  # random generator initialization
N = 10  # Number of points, initially set to 1000


def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(points)

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        q = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        # print "Computed {} from: {} {} {}".format(q, o, a, b)
        return q <= 0

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p):
            q = lower.pop()
            print "{} (removed the point {})".format(lower, q)
        lower.append(p)
        print lower

    print "UPPER HULL"

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    return lower[:-1] + upper[:-1]


def make_right_turn(o, a, b):
    """Return true if the line drawn through p1, p2 and p3 makes a right turn."""
    q = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    return (q <= 0)


def compute_convex_hull_part(result_set, for_range, point_set):
    for i in for_range:
        result_set.append(point_set[i])
        while (
            len(result_set) > 2 and
            make_right_turn(result_set[-3], result_set[-2], result_set[-1])
        ):
            q = result_set.pop(-2)
            # print "{} (removed the point {})".format(result_set, q)
    return result_set


def compute_convex_hull(cv_points):
    """Compute the convex hull of the passed points using the passed points."""
    cv_points.sort()

    L_upper = compute_convex_hull_part(cv_points[0:2], range(2, len(cv_points)), cv_points)
    print L_upper

    # L_lower = cv_points[-2:]
    # for i in reversed(range(2, len(cv_points))):
    #     L_lower.append(cv_points[i])
    #     if (len(L_lower) > 2):
    #         [p1, p2, p3] = L_lower[-3:]
    #         if (not make_right_turn(p1, p2, p3)):
    #             L_lower.remove(p2)

    # return(L_upper + L_lower[1:len(L) - 1])
    # TODO van het for stuk functie maken!


def generate_points(debug=False):
    if(debug):
        points.extend([
            [050, 700], [200, 600], [100, 400],
            [300, 200], [400, 100], [500, 100],
            [600, 300], [700, 050], [800, 100],
            [900, 500],
        ])
    else:
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
    glPointSize(10)
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
    print(convex_hull(points))
    print '---'
    print(compute_convex_hull(points))

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
