"""
In this program the intersection of two convex polygons is calculated.

It is based on the article
COMPUTER GRAPHICS AND IMAGE PROCESSING 19, 384-391 (1982)
A New Linear Algorithm for Intersecting Convex Polygons
JOSEPH O ROURKE, CHI BIN CHIEN, THOMAS OLSON, AND DAVID NADDOR
h.bekker@rug.nl
"""
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Get it at: http://atrpms.net/'''
    exit(2)

from convexPolygonIntersection import ConvexPolygonIntersection


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

P = [[50, 200], [250, 200], [250, 500]]
Q = [[150, 100], [500, 300], [150, 300]]

intersection = None

width = 700  # screen x_size
height = 700  # screen y_size


def display():
    """."""
    def get_edges(vertices):
        """Return a list of edges."""
        shifted = vertices[1:]
        shifted.append(vertices[0])
        return zip(vertices, shifted)

    glClear(GL_COLOR_BUFFER_BIT)
    # draw convex hull P
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    for (a, b) in get_edges(intersection.P):
        glVertex2f(a[0], a[1])
        glVertex2f(b[0], b[1])
    glEnd()
    glLineWidth(4)  # draw active edge of P
    # glBegin(GL_LINES)
    # glVertex2f(pd[0][0], pd[0][1])
    # glVertex2f(pd[1][0], pd[1][1])
    # glEnd()
    # draw convex hull Q
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    for (a, b) in get_edges(intersection.Q):
        glVertex2f(a[0], a[1])
        glVertex2f(b[0], b[1])
    glEnd()
    glLineWidth(4)  # draw active edge of Q
    # glBegin(GL_LINES)
    # glVertex2f(qd[0][0], qd[0][1])
    # glVertex2f(qd[1][0], qd[1][1])
    # glEnd()
    glutSwapBuffers()  # display


def keyboard(key, x, y):
    """."""
    if key == 'n':
        print "next step"
        intersection.next()
    if key in ['q', 'Q']:
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
    if argv is None:
        argv = sys.argv
    global intersection
    intersection = ConvexPolygonIntersection(P, Q)
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


if __name__ == '__main__':
    sys.exit(main())
