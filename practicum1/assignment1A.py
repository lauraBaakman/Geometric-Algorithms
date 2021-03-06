"""
This example is given to get started with python and opengl in python.

 Some random points are generated, sorted, connected by line segments and visualized
 H.Bekker@rug.nl
"""


from sys import *
from random import *
from math import sqrt
import operator
from pdb import *
# from CGAL.Kernel import *

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    exit(2)

# globals
points = []  # points
spoints = []  # x_sorted points
width = 800  # screen x_size
height = 800  # screen y_size
seed(5)  # seed value of random


def generate_points():
    for i in range(60):
        x = random()
        y = random()
        r = (x * x + y * y)
        if r > 0.5 and r < 1.0:
            points.append([500 * x + 100, 500 * y + 100])
        # print "points", points


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw points
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()
    glColor3f(1.0, 0.0, 0.0)
    # Draw lines
    glBegin(GL_LINES)
    for i in range(len(spoints) - 1):
        glVertex2f(spoints[i][0], spoints[i][1])
        glVertex2f(spoints[i + 1][0], spoints[i + 1][1])
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


def euclidean_distance(a, b):
    """Compute the euclidean distance between the n-dimensional points a and b."""
    return(
        sqrt(
            sum(
                [(a_i - b_i)**2 for a_i, b_i in zip(a, b)]
            )
        )
    )


def length_of_connecting_path(points):
    """Compute the length of the polygonal line that connects consecutive points."""
    pairs = zip(points, points[1:])
    return(
        sum(
            [euclidean_distance(a, b) for (a, b) in pairs]
        )
    )


def main(argv=None):
    if argv is None:
        argv = sys.argv
    generate_points()
    global spoints
    spoints = sorted(points, key=operator.itemgetter(0))  # sort points in x direction

    print "Length of the path between consecutive points: {}".format(
        length_of_connecting_path(spoints)
    )

    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Example1")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()
    return


if __name__ == '__main__':
    sys.exit(main())
