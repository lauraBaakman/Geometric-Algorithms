""" h.bekker@rug.nl.

Global variables:
    xa:     X-coordinates of the triangulated points in an array.
    xl:     X-coordinates of the triangulated points in a list.
    cens:   Array with a list of list where each sublist contains the coordinates
            of center of one of the triangles of the triangulation.
    edges:  Array with a list of list where each sublist contains the indices
            of the points between which one of the edges of the triangulation runs.
    triPts: Array with triangles, each triangle is represented as a list of three
            indices into xa and ya. Sorted in CW order.
    neighs:  Array of integers giving the indices into cens
            triPts, and neighs of the neighbors of each triangle.
"""
from random import *
from math import *
import sys


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

from dcel import DCEL

pi = 3.14159265358979323846
width = 700
height = 700
points = []
seed(505)  # seed value of random

ls = []
xl, yl, xyl, xa, ya, cens, edgs, triPts, neighs = [], [], [], [], [], [], [], [], []
trWithPoint = []
dcel = None


def generate_points(debug=False):
    """."""
    global xl, yl
    if(debug):
        xl = [000, 550, 250, 750]
        yl = [700, 500, 200, 000]
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
    """Display the Delaunay triangulation."""
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


def display_outer_boudary():
    """Display the Delaunay triangulation and its outer boundary."""
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
    # Draw the outer boundary
    global dcel
    face = [face for face in dcel.faces if face.inner_components]
    edges = face[0].get_edges_inner_component()
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    for edge in edges:
        destination = edge.get_destination().as_points()
        glVertex2f(edge.origin.as_points()[0], edge.origin.as_points()[1])
        glVertex2f(destination[0],  destination[1])
    glEnd()
    glutSwapBuffers()


def display_inspect_convex_hull():
    """Display the convex hull of the points and show that it is the actual convex hull."""
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw lines between all points
    glColor3f(1.0, 0.4, 0.7)
    glBegin(GL_LINES)
    for (x1, y1) in zip(xl, yl):
        for (x2, y2) in zip(xl, yl):
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
    glEnd()
    # Draw points
    glLineWidth(1.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(xl)):
        glVertex2f(xl[i], yl[i])
    glColor3f(0.0, 0.0, 1.0)
    glEnd()
    # Draw the outer boundary
    global dcel
    face = [face for face in dcel.faces if face.inner_components]
    edges = face[0].get_edges_inner_component()
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    for edge in edges:
        destination = edge.get_destination().as_points()
        glVertex2f(edge.origin.as_points()[0], edge.origin.as_points()[1])
        glVertex2f(destination[0],  destination[1])
    glEnd()
    glutSwapBuffers()


def display_circumscribed_circles():
    """Display the circumscribed circle of three triangles."""
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw Delaunay Triangulation
    glLineWidth(1.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(len(edgs)):
        glVertex2f(xl[edgs[i][0]],  yl[edgs[i][0]])
        glVertex2f(xl[edgs[i][1]],  yl[edgs[i][1]])
    glEnd()
    # Draw points
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(len(xl)):
        glVertex2f(xl[i], yl[i])
    glColor3f(0.0, 0.0, 1.0)
    glEnd()
    # Draw circles
    global dcel
    triangle_idxs = sample(
        xrange(len([face for face in dcel.faces if face.outer_component])), 3)
    for triangle_idx in triangle_idxs:
        triangle = dcel.faces[triangle_idx]
        vertex = triangle.outer_component.origin.as_points()
        center = triangle.circumcentre
        radius = sqrt((vertex[0] - center[0]) ** 2 + (vertex[1] - center[1]) ** 2)
        draw_circle(center, radius)
    glutSwapBuffers()


def display_delaunay_and_voronoi():
    """Display the Delaunay triangulation and the Vornonoi diagram."""
    global dcel
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw Delaunay Triangulation
    glLineWidth(1.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(len(edgs)):
        glVertex2f(xl[edgs[i][0]],  yl[edgs[i][0]])
        glVertex2f(xl[edgs[i][1]],  yl[edgs[i][1]])
    glEnd()
    # Draw Voronoi
    #
    # Draw Voronoi Vertices
    glColor3f(0.4, 0.4, 1.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for bounded_face in dcel.get_bounded_faces():
        circumcentre = bounded_face.circumcentre
        glVertex2f(circumcentre[0], circumcentre[1])
    # glColor3f(0.0, 0.0, 1.0)
    glEnd()
    # Draw Deaunay Vertices
    glColor3f(1.0, 0.4, 0.4)
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(len(xl)):
        glVertex2f(xl[i], yl[i])
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


def main(displayFunction, argv=None, ):
    """."""
    global xl, yl, xyl, xa, ya, cens, edgs, tris, neighs, triPts, dcel
    if argv is None:
        argv = sys.argv
    generate_points(True)
    xa = numpy.array(xl)  # transform array data to list data (for delaunay())
    ya = numpy.array(yl)
    cens, edgs, triPts, neighs = triang.delaunay(xa, ya)
    # Generate the DCEL
    dcel = DCEL.from_delaunay_triangulation(xl, yl, triPts, cens)
    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Delaunay triangulation")
    glutDisplayFunc(displayFunction)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
    return

if __name__ == '__main__':
    opts = sys.argv[1:]
    if opts and opts[0] == '-ch':
        print (
            "Showing that the boundary of the Delaunay triangulation"
            " is the convex hull of the triangulated points."
        )
        main(display_inspect_convex_hull)
    elif opts and opts[0] == '-dt':
        print "Showing the Delauny triangulation and colouring its boundary."
        main(display_outer_boudary)
    elif opts and opts[0] == '-circle':
        print "Drawing the circumscribed circle for three random triangles."
        main(display_circumscribed_circles)
    elif opts and opts[0] == '-voronoi':
        print "Draw the Delauny triangulation and the Vornonoi diagram."
        main(display_delaunay_and_voronoi)
    else:
        print (
            "Showing the Delauny triangulation. To show other visualizations"
            "use one of the following flags:\n"
            "\t-dt: The Delauny Triangulation with the outer boundary highlighted (assignment A)\n"
            "\t-ch: The outer boundary of the Delauny triangulation, its vertices and"
            "all possible line segments between the vertices. (assignment A)\n"
            "\t-circle: Draw circumscribed circles for three triangles."
        )
        main(display)
