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
import sys
from sys import *
import string
from random import *
from math import *
# import operator
import matplotlib.delaunay as triang
import numpy
import pdb

from assignment3A import find_containing_triangle
from linesegment import line_segments_intersect
from plane import project_point_on_plane

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print '''ERROR: PyOpenGL not installed properly.'''
    print '''Go get it: http://atrpms.net/'''
    exit(2)

width = 850  # screen width
height = 850  # sreen height
seed(505)  # seed value of random
ls = []

# globals
xl, yl, zl, xyl, xyzl, xa, ya = [], [], [], [], [], [], []
cens, edgs, triPts, neighs, isEdges, isL, triNormal = [], [], [], [], [], [], []
p0 = [200, 566]
p1 = [550, 200]
lightOnePosition = (400, 400, 400.0, 0.0)
lightOneColor = (0.99, 0.99, 0.99, 1.0)
dl = 0  # display list
rot = 0  # rotation used in openGL Press x or z, see keyboard function

# The 3D linesegments and triangles of the path from p0 to p1
path_edges, path_triangles = [], []


def read_points():
    """."""
    fin = open("mntElkSampledScaled2.txt")
    for line in fin:
        line = line.strip()
        b = string.split(line)
        xl.append(float(b[0]))
        yl.append(float(b[1]))
        zl.append(float(b[2]))


def generate_points(debug=False):
    """."""
    if(debug):
        global xl, yl, zl
        xl = [150, 200, 250, 450, 600, 0, 0, 640]
        yl = [550, 450, 500, 100, 550, 0, 650, 10]
        zl = [100, 200, 150, 80, 250, 40, 50, 200]
        print "Points: {}".format([xyz for xyz in zip(xl, yl, zl)])
    else:
        nPoints = 100
        for i in range(nPoints):
            x = 600 * random() + 50
            y = 600 * random() + 50
            r = sqrt((x - 300)**2 + (y - 300)**2)
            z = 300 - 40 * cos(r / 50)
            xl.append(x)
            yl.append(y)
            zl.append(z)


def pInTriangle(p, a, b, c):
    """Return true if the point p is in the triangle defined by a, b and c."""
    nom = (a[1] * b[0] - a[0] * b[1] - a[1] * c[0] + b[1] * c[0] + a[0] * c[1] - b[0] * c[1])
    if nom:
        l1 = -((-(b[1]*c[0]) + b[0]*c[1] + b[1]*p[0] - c[1]*p[0] - b[0]*p[1] + c[0]*p[1])/nom)
        l2 = -((a[1]*c[0] - a[0]*c[1] - a[1]*p[0] + c[1]*p[0] + a[0]*p[1] - c[0]*p[1])/nom)
    return(l1 >= 0 and l1 <= 1 and l2 >= 0 and l2 <= 1 and 1-l1-l2 >= 0 and 1-l1-l2 <= 1)


def display3D():
    """."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    # look from above at an angle  360-40
    glRotatef(360-40, 1.0, 0.0, 0.0)
    # rotate over angle rot
    glRotatef(rot, 0.0, 0.0, 1.0)
    if dl:
        glCallList(dl)
    glPopMatrix()
    glutSwapBuffers()


def generate_dl():
    """Display list."""
    global dl
    dl = glGenLists(1)
    glNewList(dl, GL_COMPILE)
    glColor3f(0.0, 1.0, 1.0)

    # scale factor
    sf = 0.005
    glScalef(sf, sf, sf)

    # draw all triangles
    glTranslatef(-300.0, -300.0, -300.0)
    glColor3f(0.1, 0.7, 0.3)
    glBegin(GL_TRIANGLES)
    for i in range(len(triPts)):
        glNormal3fv(triNormal[i])
        glVertex3fv(xyzl[triPts[i][0]])
        glVertex3fv(xyzl[triPts[i][1]])
        glVertex3fv(xyzl[triPts[i][2]])
    glEnd()

    # draw path
    glColor3f(0.99, 0.3, 0.3)
    glLineWidth(3)
    glBegin(GL_LINES)
    for edge in path_edges:
        glVertex3f(edge[0][0], edge[0][1], edge[0][2])
        glVertex3f(edge[1][0], edge[1][1], edge[1][2])
    glEnd()
    glEndList()


def reshape3D(w, h):
    """."""
    glViewport(0, 0,  width,  height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, (w + 0.0)/h, 0.2, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def oprod(a, b):
    """Compute the outer product of a and b."""
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def normalize(v):
    """Normalize the vector v."""
    l = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    linv = 1/l
    return [linv*v[0], linv*v[1], linv*v[2]]


def normal(p0, p1, p2):
    """ Calculate the normal vector of the plane defined by three points."""
    v1 = [p0[0]-p1[0], p0[1]-p1[1], p0[2]-p1[2]]
    v2 = [p0[0]-p2[0], p0[1]-p2[1], p0[2]-p2[2]]
    v1Ov2 = oprod(v1, v2)
    return normalize(v1Ov2)


def length_2(a, b):
    """."""
    l = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return l


def length_3(a, b):
    """."""
    l = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    return l


def keyboard(key, x, y):
    """Increase, decrease the rotation angle."""
    global rot
    # x
    if key == chr(120):
        rot = (rot+2) % 360
        glutPostRedisplay()
    # z
    if key == chr(122):
        rot = (rot-2) % 360
        glutPostRedisplay()
    # Q
    if key == 'Q':
        raise SystemExit


def main(argv=None):
    """."""
    global xl, yl, zl, xyl, xa, ya, cens, edgs, tris, neighs, triPts, trWithPoint
    # global width, height
    if argv is None:
        argv = sys.argv
    # generate_points()
    read_points()

    for i in range(len(xl)):
        xyl.append([xl[i], yl[i]])
        xyzl.append([xl[i], yl[i], zl[i]])
    # transform array data to list data (for delaunay())
    xa = numpy.array(xl)
    ya = numpy.array(yl)
    cens, edgs, triPts, neighs = triang.delaunay(xa, ya)
    intersections = 0
    for i in range(len(triPts)):
        triNormal.append(normal(xyzl[triPts[i][0]], xyzl[triPts[i][1]], xyzl[triPts[i][2]]))
    find_path()
    print("Path length: {}".format(path_length(path_edges)))
    print("Line segments: {}".format(path_edges))
    glutInit(argv)
    glutInitWindowSize(width, height)
    glutCreateWindow("Mount Elk")
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_COLOR_MATERIAL)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glEnable(GL_DEPTH_TEST)
    glutInitWindowPosition(100, 100)
    glLightfv(GL_LIGHT0, GL_POSITION, lightOnePosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightOneColor)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_RESCALE_NORMAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)
    glutDisplayFunc(display3D)
    glutReshapeFunc(reshape3D)
    glutKeyboardFunc(keyboard)
    generate_dl()
    glutMainLoop()
    return


def find_neighbouring_edge_intersected_by_s(triangle_idx):
    """Find the the 2 and 3d intersection point along s on the edge neighbouring triangle_idx."""
    for n in (x for x in neighs[triangle_idx] if x not in path_triangles):
        shared_edge = list(set(triPts[triangle_idx]).intersection(set(triPts[n])))
        intersection_point_2d = line_segments_intersect(
            [[xl[shared_edge[0]], yl[shared_edge[0]]],
             [xl[shared_edge[1]], yl[shared_edge[1]]]], [p0, p1]
        )
        if(intersection_point_2d):
            intersection_point_3d = project_point_on_plane(get_triangle(n), intersection_point_2d)
            return (n, intersection_point_3d)

    raise AssertionError("No neighbouring edge could be found...")


def get_triangle(triPts_idx):
    """Return a triangle as a list of 2D points based on its index in triPts/neighs/cens."""
    (p1, p2, p3) = triPts[triPts_idx]
    return ([
        [xl[p1], yl[p1], zl[p1]],
        [xl[p2], yl[p2], zl[p2]],
        [xl[p3], yl[p3], zl[p3]]
    ])


def find_path():
    """Find the path from p0 to p1 in the triangulation."""
    # Find the triangles containing p0 and p1
    (t0, _) = find_containing_triangle(p0, triPts, xl, yl)
    (t1, _) = find_containing_triangle(p1, triPts, xl, yl)

    global path_edges, path_triangles

    # Current triangle while finding the path
    t = t0

    # Current point while finding the path
    p = project_point_on_plane(get_triangle(t0), p0)
    path_triangles.append(-1)
    path_triangles.append(t)

    while t != t1:
        e0 = p
        (t, p) = find_neighbouring_edge_intersected_by_s(t)
        path_triangles.append(t)
        path_edges.append([e0, p])
    path_triangles.pop(0)
    path_edges.append([
        p,
        project_point_on_plane(get_triangle(t1), p1)
    ])


def euclidean_distance(a, b):
    """Compute the euclidean distance between the n-dimensional points a and b."""
    return(sqrt(sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)])))


def path_length(edges):
    """Compute the length, using euclidean distance of the path defined by the edges."""
    return(sum([euclidean_distance(p1, p2) for [p1, p2] in edges]))

if __name__ == '__main__':
    sys.exit(main())
