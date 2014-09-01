"""
This example is given to get started with python and opengl in python.

Some random points are generated, sorted, connected by line segments and visualized.
H.Bekker@rug.nl
"""


from sys import *
from random import *
import operator


try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Go get it: http://atrpms.net/'''
    exit(2)

# globals
points = []  # points
spoints = []  # x_sorted points
width = 800  # screen x_size
height = 800  # screen y_size
seed(5)  # seed value of random


def generate_points():
    """Generate points."""
    for i in range(60):
        x = random()
        y = random()
        r = (x * x + y * y)
        if r > 0.5 and r < 1.0:
            points.append([500 * x + 100, 500 * y + 100])


def display():
    """OpenGL display function."""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw points
    # Set the colour of the points to green
    glColor3f(0.0, 1.0, 0.0)

    # Set the size of the points
    glPointSize(3)

    # Draw the points
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

    # Draw lines
    # Set the colours of the lines to red
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINES)
    for i in range(len(spoints) - 1):
        glVertex2f(spoints[i][0], spoints[i][1])
        glVertex2f(spoints[i + 1][0], spoints[i + 1][1])
    glEnd()
    glutSwapBuffers()  # display


def reshape(wid, hgt):
    """OpenGL reshape function."""
    global width, height
    width = wid
    height = hgt
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # reshape
    gluOrtho2D(0, width, height, 0)


def main(argv=None):
    """Main function."""
    if argv is None:
        argv = sys.argv
    generate_points()
    global spoints
    # sort points in x direction
    spoints = sorted(points, key=operator.itemgetter(0))
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
