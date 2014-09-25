import sys
from sys import *
import string 
from random import *
from math import *
import operator
import matplotlib.delaunay as triang
import numpy

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''ERROR: PyOpenGL not installed properly.'''
  print '''Go get it: http://atrpms.net/'''
  exit ( 2 ) 

width  = 850  # screen width
height = 850  # sreen height
seed(505)  # seed value of random
ls=[]
# globals
xl, yl, zl, xyl, xyzl, xa, ya, cens, edgs, triPts, neighs, isEdges, isL, triNormal =[], [], [], [], [],[],[],[], [], [], [], [], [], []
p0=[200,566]
p1=[550,200]
lightOnePosition = (400, 400, 400.0, 0.0)
lightOneColor = (0.99, 0.99, 0.99, 1.0) 
dl=0  # display list
rot=0  # rotation used in openGL Press x or z, see keyboard function

def read_points():
    fin =open("mntElkSampledScaled2.txt")
    for line in fin:
      line = line.strip()
      b=string.split(line)
      xl.append(float(b[0]))
      yl.append(float(b[1]))
      zl.append(float(b[2]))
      
def generate_points():
   for i in range(100):
      x=600*random()+50
      y=600*random()+50
      r=sqrt((x-300)**2 + (y-300)**2)
      z=300 - 40* cos(r/50)
      xl.append(x)
      yl.append(y)
      zl.append(z)
 
def pInTriangle(p,a,b,c): # is point p in the triangle defined by a,b,c?
   nom=(a[1]*b[0] - a[0]*b[1] - a[1]*c[0] + b[1]*c[0] + a[0]*c[1] - b[0]*c[1])
   if nom!=0.0:
     l1=-((-(b[1]*c[0]) + b[0]*c[1] + b[1]*p[0] - c[1]*p[0] - b[0]*p[1] + c[0]*p[1])/nom)
     l2=-((a[1]*c[0] - a[0]*c[1] - a[1]*p[0] + c[1]*p[0] + a[0]*p[1] - c[0]*p[1])/nom)
   return (l1>=0 and l1 <=1 and l2 >=0 and l2<=1 and 1-l1-l2>=0 and 1-l1-l2<=1)
   
def display3D():
  glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glPushMatrix()
  # look from above at an angle  360-40
  glRotatef (360-40,1.0,0.0,0.0)
  # rotate over angle rot
  glRotatef ( rot, 0.0, 0.0, 1.0)
  if dl!=0:
    glCallList(dl)
  glPopMatrix()
  glutSwapBuffers()
  
def generate_dl():  # display list
  global dl
  dl=glGenLists(1)
  glNewList(dl, GL_COMPILE)
  glColor3f (0.0, 1.0, 1.0)
  sf=0.005  # scale factor
  glScalef (sf,sf,sf)
  #draw all triangles 
  glTranslatef(-300.0,-300.0,-300.0)
  glColor3f (0.1, 0.7, 0.3)
  glBegin(GL_TRIANGLES)
  for i in range(len(triPts)):
    glNormal3fv(triNormal[i])
    glVertex3fv(xyzl[triPts[i][0]])
    glVertex3fv(xyzl[triPts[i][1]])
    glVertex3fv(xyzl[triPts[i][2]])
  glEnd()
  #draw fictitious path
  glColor3f (0.99, 0.3, 0.3)      
  glLineWidth(3)
  glBegin (GL_LINES)
  for i in range(2):
     glVertex3f (p0[0], p0[1], 250.0 ) # the height 250.0 is fictitious
     glVertex3f (p1[0], p1[1], 250.0  ) # you have to calculate the correct path
  glEnd()
  glEndList()

def reshape3D (w,h):
  glViewport (0, 0,  width,  height) 
  glMatrixMode (GL_PROJECTION)
  glLoadIdentity ()
  gluPerspective(60.0,  w/h, 0.2, 10.0)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity();
  gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
  
def oprod(a,b):  # outer product of a and b
   return [ a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0] ]

def normalize(v):  # normalize the vector v
    l=sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    linv=1/l
    return [linv*v[0], linv*v[1], linv*v[2]]

def normal(p0,p1,p2):  # calculate the normal vector of the plane defined by three points
    v1=[p0[0]-p1[0], p0[1]-p1[1], p0[2]-p1[2]]
    v2=[p0[0]-p2[0], p0[1]-p2[1], p0[2]-p2[2]]
    v1Ov2=oprod(v1,v2)
    return normalize(v1Ov2)

def length_2(a,b):
    l=sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) 
    return l
 
def length_3(a,b):
    l=sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) 
    return l

def keyboard (key,x,y):  # increase, decrease the rotation angle
   global rot 
   if key==chr(120) : #x
      rot=(rot+2) % 360
      glutPostRedisplay()
   if key==chr(122) : #z
      rot=(rot-2) % 360
      glutPostRedisplay()

def main (argv=None):
    global xl,yl, zl, xyl, xa,ya, cens, edgs, tris, neighs, triPts, trWithPoint
    if argv is None:
      argv = sys.argv
    generate_points()
    #read_points()
    for i in range(len(xl)): 
      xyl.append([xl[i], yl[i]])
      xyzl.append([xl[i], yl[i], zl[i]])
    xa = numpy.array(xl)# transform array data to list data (for delaunay())
    ya = numpy.array(yl)
    cens,edgs,triPts,neigs = triang.delaunay(xa,ya)
    intersections=0
    for i in range(len(triPts)):
      triNormal.append(normal(xyzl[triPts[i][0]], xyzl[triPts[i][1]], xyzl[triPts[i][2]]))
      
    glutInit(argv)
    glClearDepth (1.0)
    glEnable (GL_DEPTH_TEST)
    glClearColor (1.0, 1.0, 1.0, 0.0)
    glShadeModel (GL_FLAT)
    glEnable(GL_COLOR_MATERIAL)
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB  | GLUT_DEPTH)
    glEnable(GL_DEPTH_TEST)
    glutInitWindowSize (width, height)
    glutInitWindowPosition (100, 100)
    glutCreateWindow ("Mount Elk")
    glLightfv (GL_LIGHT0, GL_POSITION, lightOnePosition)
    glLightfv (GL_LIGHT0, GL_DIFFUSE, lightOneColor)
    glEnable (GL_LIGHT0)
    glEnable (GL_LIGHTING)
    glEnable(GL_RESCALE_NORMAL)
    glColorMaterial (GL_FRONT_AND_BACK, GL_DIFFUSE)
    glEnable (GL_COLOR_MATERIAL)
    glutDisplayFunc(display3D)
    glutReshapeFunc (reshape3D)
    glutKeyboardFunc(keyboard)
    generate_dl()
    glutMainLoop()
    return

if __name__=='__main__':
    sys.exit(main())
