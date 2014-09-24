"""
In this program the intersection of two convex polygons is calculated.

It is based on the article
COMPUTER GRAPHICS AND IMAGE PROCESSING 19, 384-391 (1982)
A New Linear Algorithm for Intersecting Convex Polygons
JOSEPH O ROURKE, CHI BIN CHIEN, THOMAS OLSON, AND DAVID NADDOR
h.bekker@rug.nl
"""
import pdb
import random

from linesegment import LineSegment

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Get it at: http://atrpms.net/'''
    exit(2)


# P and Q are two convex polygons. Points are given in counter clockwise order
P = [
    [63.825904920238017, 238.51837485295556],
    [146.61946774658253, 150.83681845731257],
    [187.38195814743474, 108.33595920368576],
    [429.49486383026618, 66.375164737529488],
    [520.43126692251815, 82.725295508808841],
    [625.61917430353492, 209.15222849770743],
    [656.16718379928432, 334.0672530084903],
    [608.9378767228128, 481.83586981034904],
    [547.19440784683934, 578.7637127538934],
    [524.85651560389124, 591.41662257169071],
    [427.57927666483698, 642.66102987331851],
    [237.97166863809122, 646.93833359945347],
    [137.56516935910571, 529.0154887159224],
    [85.320208683916846, 435.1806355460111],
    [75.542837591689178, 396.06840939472079],
]
Q = [
    [59.670349219872577, 467.56725106509288],
    [75.750302986414638, 265.43933914503634],
    [80.980773993593175, 218.20228053820173],
    [114.34724735535217, 168.37321164423099],
    [278.12323903354905, 42.097123217066709],
    [417.21085385330292, 72.49413422357479],
    [498.71035610431852, 94.238122521617683],
    [589.44384668506336, 153.46247650823628],
    [640.49410194013012, 322.69798679172101],
    [644.91176466163517, 418.80055705278971],
    [627.26298645240263, 457.86868079173047],
    [330.21222050606116, 661.78306198998234],
    [161.01348092439304, 573.71561497179664]
]

# Degenerate instance of P. The first 3 points of P have been removed.
# To test the algorithm for a degenerate problem instance calculate
# the intersection of P and degP
degP = [
    [429.49486383026618, 66.375164737529488],
    [520.43126692251815, 82.725295508808841],
    [625.61917430353492, 209.15222849770743],
    [656.16718379928432, 334.0672530084903],
    [608.9378767228128, 481.83586981034904],
    [547.19440784683934, 578.7637127538934],
    [524.85651560389124, 591.41662257169071],
    [427.57927666483698, 642.66102987331851],
    [237.97166863809122, 646.93833359945347],
    [137.56516935910571, 529.0154887159224],
    [85.320208683916846, 435.1806355460111],
    [75.542837591689178, 396.06840939472079]
]

P_test = [
    [600.0, 900.0],
    [200.0, 900.0],
    [200.0, 300.0],
    [600.0, 300.0],
]
Q_test = [
    [400.0, 600.0],
    [100.0, 600.0],
    [100.0, 100.0],
    [400.0, 100.0],
]

# p and q are the active vertices of P and Q, p_minus, q_minus, p_Dot, q_Dot
p, q, p_min, q_min, p_dot, q_dot = 0, 0, 0,  0, 0, 0
pg = None
intersection_points = []

width = 700  # screen x_size
height = 1000  # screen y_size


class PolygonIntersection(object):

    """
    Class that computes the intersection of two polygons.

    Polygons are represented as a list of points in counter clockwise
    order.

    This class is an Iterator so that the algorithm may be executed
    step by step.

    """

    def __init__(self, set_P, set_Q):
        """Construct a PolygonIntersection object."""
        super(PolygonIntersection, self).__init__()
        global P, Q
        P = set_P
        Q = set_Q
        self._current_step = 1
        self._max_steps = 2 * (len(P) + len(Q))
        self._first_intersection = None

        self._algorithm_init()

    def __iter__(self):
        """Make this class iterable."""
        return self

    def next(self):
        """Take the next step."""
        print "\nStep {}".format(self._current_step)
        global intersection_points
        if self._current_step <= self._max_steps:
            self._current_step = self._current_step + 1
            points = self._algorithm_step()
            intersection_points.extend(points)
        else:
            points = self._algorithm_finalize()
            intersection_points.extend(points)
            raise StopIteration(
                "Terminated the algorithm, since more than 2 * |P| * |Q| steps have been taken."
            )

    def _algorithm_finalize(self):
        """Finalize the algorithm, is called when no intersection was found."""
        p = random.randint(0, len(P) - 1)
        q = random.randint(0, len(Q) - 1)

    def _point_in_polygon(point, polygon):
        """Test if the point lies in the polygon."""
        def intersecting_vectors(v1, v2):
            """Test if the line through """





    def _algorithm_step(self):
        """Execute one iteration of the do-while of the algorithm."""
        def in_half_plane(x, plane_dot):
            """Test if the point x is in the half plane defined by plane_dot and plane_min."""
            return (
                -(plane_dot[0][1] * plane_dot[1][0]) + plane_dot[0][0] * plane_dot[1][1] +
                plane_dot[0][1] * x[0] - plane_dot[1][1] * x[0] -
                plane_dot[0][0] * x[1] + plane_dot[1][0] * x[1]
                >= 0
            )

        def advance(advancing_set, inside):
            """Handle the advancement of the active edge."""
            def advance_p():
                """Advance p."""
                global p, p_min, p_dot
                if (inside == 'p'):
                    return_points.append(p)
                p = (p + 1) % len(P)
                p_min = (p - 1 + len(P)) % len(P)
                p_dot = [P[p_min], P[p]]

            def advance_q():
                """Advance q."""
                global q, q_min, q_dot
                if (inside == 'q'):
                    return_points.append(q)
                q = (q + 1) % len(Q)
                q_min = (q - 1 + len(Q)) % len(Q)
                q_dot = [Q[q_min], Q[q]]

            {
                'p': advance_p,
                'q': advance_q
            }.get(advancing_set)()

        intersection = LineSegment.from_point_list(p_dot).intersect(
            LineSegment.from_point_list(q_dot)
        )

        return_points = []
        inside = None

        if(intersection):
            if(not self._first_intersection):
                self._first_intersection = intersection
            elif(intersection == self._first_intersection):
                return []
            return_points.append(intersection)

            if(in_half_plane(P[p], q_dot)):
                inside = 'p'
            else:
                inside = 'q'

        q_dot_cross_p_dot = (
            p_dot[0][1] * q_dot[0][0] - p_dot[1][1] * q_dot[0][0] - p_dot[0][0] * q_dot[0][1] +
            p_dot[1][0] * q_dot[0][1] - p_dot[0][1] * q_dot[1][0] + p_dot[1][1] * q_dot[1][0] +
            p_dot[0][0] * q_dot[1][1] - p_dot[1][0] * q_dot[1][1]
        )
        if (q_dot_cross_p_dot >= 0):
            if(in_half_plane(P[p], q_dot)):
                advance('q', inside)
            else:
                advance('p', inside)
        else:
            if(in_half_plane(Q[q], p_dot)):
                advance('p', inside)
            else:
                advance('q', inside)
        return return_points

    def _algorithm_init(self):
        """Initialize the algorithm by selecting a random p and q."""
        global p, q, p_min, q_min, p_dot, q_dot
        p_min, q_min = len(P) - 1, len(Q) - 1
        p_dot = [P[p_min], P[p]]
        q_dot = [Q[q_min], Q[q]]


def display():
    """."""
    glClear(GL_COLOR_BUFFER_BIT)
    # draw convex hull P
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    for i in range(len(P) - 1):
        glVertex2f(P[i][0], P[i][1])
        glVertex2f(P[i + 1][0], P[i + 1][1])
    # draw edge from last to first entry in ch
    glVertex2f(P[len(P) - 1][0], P[len(P) - 1][1])
    glVertex2f(P[0][0], P[0][1])
    glEnd()
    glLineWidth(4)  # draw active edge of P
    glBegin(GL_LINES)
    glVertex2f(p_dot[0][0], p_dot[0][1])
    glVertex2f(p_dot[1][0], p_dot[1][1])
    glEnd()
    # draw convex hull Q
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    for i in range(len(Q) - 1):
        glVertex2f(Q[i][0], Q[i][1])
        glVertex2f(Q[i + 1][0], Q[i + 1][1])
    # draw edge from last to first entry in ch
    glVertex2f(Q[len(Q) - 1][0], Q[len(Q) - 1][1])
    glVertex2f(Q[0][0], Q[0][1])
    glEnd()
    glLineWidth(4)  # draw active edge of Q
    glBegin(GL_LINES)
    glVertex2f(q_dot[0][0], q_dot[0][1])
    glVertex2f(q_dot[1][0], q_dot[1][1])
    glEnd()
    glutSwapBuffers()  # display


def keyboard(key, x, y):
    """."""
    # p_min, q_min means p_minus q_minus resp., see article
    global p, q, p_min, q_min, p_dot, q_dot, intersection_points
    if key == 'p':  # advance active edge of P (test purpose)
        p += 1
        p_min = p - 1
    if p == len(P):
        p = 0
    if p_min < 0:
        p_min = len(P) - 1
    if key == 'q':  # advance active edge of Q (test purpose)
        q += 1
        q_min = q - 1
    if q == len(Q):
        q = 0
    if q_min < 0:
        q_min = len(Q) - 1
    # p_dot means "p dot" see article
    p_dot = [
        [P[p_min][0], P[p_min][1]],
        [P[p][0], P[p][1]]
    ]
    # q_dot means "q dot" see article
    q_dot = [[Q[q_min][0], Q[q_min][1]], [Q[q][0], Q[q][1]]]
    if key == 'n':  # do one step of the actual algorithm from the paper
        pg.next()
    if key == 'Q':
        raise SystemExit


def reshape(wid, hgt):
    """."""
    global width, height
    width = wid
    height = hgt
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, height, 0)  # reshape


def main(argv=None):
    """."""
    global P, Q, p_min, q_min, p_dot, q_dot, pg
    if argv is None:
        argv = sys.argv
    pg = PolygonIntersection(P_test, Q_test)
    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Intersection of two convex hulls")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    display()
    glutMainLoop()
    return


def main_without_visualization():
    """Run the program without visualization."""
    pi = PolygonIntersection(P, Q)
    while True:
        pi.next()


if __name__ == '__main__':
    sys.exit(main())
    # main_without_visualization()
