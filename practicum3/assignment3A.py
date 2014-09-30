"""
h.bekker@rug.nl.

Global variables:
    xa:     X-coordinates of the triangulated points in an array.
    xl:     X-coordinates of the triangulated points in a list.
    cens:   Array with a list of list where each sublist contains the coordinates
            of center of one of the triangles of the triangulation.
    edges:  Array with a list of list where each sublist contains the indices
            of the points between which one of the edges of the triangulation runs.
    triPts: Array with triangles, each triangle is represented as a list of three
            indices into xa and ya.
    neighs:  Array of integers giving the indices into cens
            triPts, and neighs of the neighbors of each triangle.
"""

from random import *
import matplotlib.delaunay as triang
import numpy
from triangle import point_in_triangle


try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Go get it: http://atrpms.net/'''
    exit(2)

width = 700
height = 700
points = []
seed(505)  # seed value of random
lp = [305, 350]

xl, yl, xyl, xa, ya, cens, edgs, triPts, neighs = [], [], [], [], [], [], [], [], []
trWithPoint = []


def generate_points(debug=False):
    """."""
    global xl, yl
    if(debug):
        xl = [150, 200, 250, 450, 600, 0]
        yl = [550, 450, 500, 100, 550, 0]
        print "Points: {}".format([xy for xy in zip(xl, yl)])
    else:
        number_of_points = 100
        for i in range(number_of_points):
            x = 600 * random() + 50
            y = 600 * random() + 50
            xl.append(x)
            yl.append(y)


def display():
    """."""
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw points
    glLineWidth(1.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(xl)):
        print "xl[i]", xl[i]
        glVertex2f(xl[i], yl[i])

    # Draw the point
    glColor3f(0.0, 0.7, 1.0)
    glVertex(lp[0], lp[1])
    glEnd()

    # Draw Delaunay Triangulation
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_LINES)
    for i in range(len(edgs)):
        glVertex2f(xl[edgs[i][0]],  yl[edgs[i][0]])
        glVertex2f(xl[edgs[i][1]],  yl[edgs[i][1]])

    # Draw containing triangle
    glColor3f(0.0, 0.7, 1.0)
    (_, containing_triangle) = find_containing_triangle(lp, triPts, xl, yl)
    glVertex2f(xl[containing_triangle[0]],  yl[containing_triangle[0]])
    glVertex2f(xl[containing_triangle[1]],  yl[containing_triangle[1]])

    glVertex2f(xl[containing_triangle[0]],  yl[containing_triangle[0]])
    glVertex2f(xl[containing_triangle[2]],  yl[containing_triangle[2]])

    glVertex2f(xl[containing_triangle[1]],  yl[containing_triangle[1]])
    glVertex2f(xl[containing_triangle[2]],  yl[containing_triangle[2]])

    glEnd()
    glutSwapBuffers()


def reshape(wid, hgt):
    """."""
    global width, height
    width = wid
    height = hgt
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, height, 0)


def keyboard(key, x, y):
    """Handle keyboard events."""
    print key
    if key == 'Q':
        raise SystemExit


def main(argv=None):
    """."""
    global xl, yl, xyl, xa, ya, cens, edgs, triPts, lp
    if argv is None:
        argv = sys.argv
    generate_points(True)
    for i in range(len(xl)):
        xyl.append([xl[i], yl[i]])
    xa = numpy.array(xl)  # transform array data to list data (for delaunay())
    ya = numpy.array(yl)
    cens, edgs, triPts, neigs = triang.delaunay(xa, ya)
    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Delaunay triangulation")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
    return


def find_containing_triangle(p, triPts=triPts, xl=xl, yl=yl):
    """
    Find the triangle of the triangulation that contains the point p.

    The triangle is returned as an index in the global array triPts and
    as three indices in the global arrays xl and yl.

    """
    for idx, triangle in enumerate(triPts):
        [p1, p2, p3] = triangle
        if(point_in_triangle(
            [
                [xl[p1], yl[p1]],
                [xl[p2], yl[p2]],
                [xl[p3], yl[p3]]
            ],
            p
        )):
            print (
                "The triangle that contains the point ({lp_x},{lp_y}):"
                "({p1_x}, {p1_y}), ({p2_x}, {p2_y}), ({p3_x}, {p3_y})"
                .format(
                    lp_x=p[0], lp_y=p[1],
                    p1_x=xl[p1], p1_y=yl[p1],
                    p2_x=xl[p2], p2_y=yl[p2],
                    p3_x=xl[p3], p3_y=yl[p3],
                )
            )
            return (idx, triangle)


if __name__ == '__main__':
    sys.exit(main())
