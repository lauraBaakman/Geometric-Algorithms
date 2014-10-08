""" h.bekker@rug.nl.

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
from math import *
import matplotlib.delaunay as triang
import numpy


try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Go get it: http://atrpms.net/'''
    exit(2)

pi = 3.14159265358979323846
width = 700
height = 700
points = []
seed(505)  # seed value of random

ls = []
xl, yl, xyl, xa, ya, cens, edgs, triPts, neighs = [], [], [], [], [], [], [], [], []
trWithPoint = []


def generate_points(debug=False):
    """."""
    global xl, yl
    if(debug):
        xl = [150, 200, 250, 450, 600, 10]
        yl = [550, 450, 500, 100, 550, 10]
        print "Points: {}".format([xy for xy in zip(xl, yl)])
    else:
        for i in range(100):
            x = 600 * random() + 50
            y = 600 * random() + 50
            xl.append(x)
            yl.append(y)
            xyl.append([x, y])


def keyboard(key, x, y):
    """Handle keyboard events."""
    print key
    if key == 'Q':
        raise SystemExit


def display():
    """."""
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw points
    glLineWidth(1.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(xl)):
        glVertex2f(xl[i], yl[i])
    glColor3f(0.0, 0.0, 1.0)
    glEnd()
    # Draw Delaunay Triangulation
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(len(edgs)):
        glVertex2f(xl[edgs[i][0]],  yl[edgs[i][0]])
        glVertex2f(xl[edgs[i][1]],  yl[edgs[i][1]])
    glEnd()
    glutSwapBuffers()


def draw_circle(c, r):
    """."""
    # draws a circle, center c, radius r
    n = 50  # nr of segments
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(5)
    for i in range(n):
        phi1, phi2 = (float(i) / n) * 2 * pi, (float(i + 1) / n) * 2 * pi
        glBegin(GL_LINES)
        glVertex2f(c[0] + r * cos(phi1),  c[1] + r * sin(phi1))
        glVertex2f(c[0] + r * cos(phi2),  c[1] + r * sin(phi2))
        glEnd()


def reshape(wid, hgt):
    """."""
    global width, height
    width = wid
    height = hgt
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, height, 0)


def main(argv=None):
    """."""
    global xl, yl, xyl, xa, ya, cens, edgs, tris, neighs, triPts
    if argv is None:
        argv = sys.argv
    generate_points(True)
    xa = numpy.array(xl)  # transform array data to list data (for delaunay())
    ya = numpy.array(yl)
    cens, edgs, triPts, neighs = triang.delaunay(xa, ya)
    # glutInit(argv)
    # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    # glutInitWindowSize(width, height)
    # glutInitWindowPosition(100, 100)
    # glutCreateWindow("Delaunay triangulation")
    # glutDisplayFunc(display)
    # glutReshapeFunc(reshape)
    # glutKeyboardFunc(keyboard)
    # glutMainLoop()
    return

if __name__ == '__main__':
    sys.exit(main())
