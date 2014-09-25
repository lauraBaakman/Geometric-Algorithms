#!/usr/bin/python
#h.bekker@rug.nl
from random import *
import matplotlib.delaunay as triang
import numpy
import operator



try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''ERROR: PyOpenGL not installed properly.'''
  print '''Go get it: http://atrpms.net/'''
  exit ( 2 ) 

width  = 850  
height = 850 
points = [] 
seed(505)  # seed value of random

ls=[]
xl, yl, xyl, xa, ya, cens, edgs, triPts, neighs =[], [],[], [], [], [], [], [], []
trWithPoint=[]
p0=[200,566]
p1=[550,200]

def generate_points():
   global xl,yl
   for i in range(100):
      x=600*random()+50
      y=600*random()+50
      xl.append(x)
      yl.append(y)

def pInTriangle(p,a,b,c): # is point p in the triangle defined by a,b,c?
   nom=(a[1]*b[0] - a[0]*b[1] - a[1]*c[0] + b[1]*c[0] + a[0]*c[1] - b[0]*c[1])
   if nom!=0.0:
     l1=-((-(b[1]*c[0]) + b[0]*c[1] + b[1]*p[0] - c[1]*p[0] - b[0]*p[1] + c[0]*p[1])/nom)
     l2=-((a[1]*c[0] - a[0]*c[1] - a[1]*p[0] + c[1]*p[0] + a[0]*p[1] - c[0]*p[1])/nom)
   return (l1>=0 and l1 <=1 and l2 >=0 and l2<=1 and 1-l1-l2>=0 and 1-l1-l2<=1)
   
def intersectSegments(s1,s2):  
    p0x, p1x, p2x, p3x =s1[0][0], s1[1][0], s2[0][0], s2[1][0] # the x coordinates of the endpoints of the segments
    p0y, p1y, p2y, p3y =s1[0][1], s1[1][1], s2[0][1], s2[1][1] # the y coordinates of the endpoints of the segments
    nom=-p0x*p2y + p0x*p3y + p1x*p2y - p1x*p3y + p2x*p0y - p2x*p1y - p3x*p0y + p3x*p1y
    if nom==0:
       intersection=False
       return intersection, [0,0]
    a_denom=p1x*p2y - p1x*p3y - p2x*p1y + p2x*p3y - p3x*p2y + p3x*p1y
    b_denom=-p1x*p3y + p3x*p1y + p0y*p1x - p3x*p0y - p1y*p0x + p0x*p3y
    a, b=a_denom/nom, b_denom/nom
    if 0.0<= a and a<=1.0 and 0.0<= b and b<=1.0:
      return True, a,b, [a*p0x+(1-a)*p1x, a*p0y+(1-a)*p1y]
    else: 
      return False, 0,0,[0.0,0.0]    
   
def display():
    glClear (GL_COLOR_BUFFER_BIT)
    # Draw points
    glLineWidth(1.0)
    glColor3f (1.0, 1.0, 1.0)
    glPointSize (3)
    glBegin(GL_POINTS)
    for i in range(len(xl)):
      #print "xl[i]", xl[i]
      glVertex2f (xl[i], yl[i])
    glColor3f (0.0, 0.0, 1.0)
    glEnd()
    # Draw Delaunay Triangulation
    glColor3f (1.0, 0.0, 0.0)
    glBegin (GL_LINES)
    for i in range(len(edgs)):
      glVertex2f ( xl[edgs[i][0]] ,  yl[edgs[i][0]])
      glVertex2f ( xl[edgs[i][1]] ,  yl[edgs[i][1]])
    # draw walk line  
    glColor3f (0.0, 1.0, 0.0)
    glVertex2f (p0[0], p0[1])
    glVertex2f (p1[0], p1[1])
    glEnd ()
    #draw intersection points on walk line

    # draw intersected segments
 
    glutSwapBuffers ()


def reshape (wid, hgt):
    global width, height
    width = wid
    height = hgt
    glViewport( 0, 0, width, height )
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluOrtho2D (0, width, height, 0)



def main (argv=None):
    global xl,yl,xyl, xa,ya, cens, edgs, tris, neighs, triPts, trWithPoint
    if argv is None:
        argv = sys.argv
    generate_points()
    #print "xl", xl
    for i in range(len(xl)): 
      xyl.append([xl[i], yl[i]])
    xa = numpy.array(xl)# transform array data to list data (for delaunay())
    ya = numpy.array(yl)
    cens,edgs,triPts,neigs = triang.delaunay(xa,ya)

    glutInit(argv)
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize (width, height)
    glutInitWindowPosition (100, 100)
    glutCreateWindow ("Delaunay triangulation")
    glutDisplayFunc(display)
    glutReshapeFunc (reshape)
    glutMainLoop()
    return

if __name__=='__main__':
    sys.exit(main())
