#!/usr/bin/env python


from random import *
from math import sqrt
import operator

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''ERROR: PyOpenGL not installed properly.'''
  print '''Get it at: http://atrpms.net/'''
  exit ( 2 ) 

# globals
points=[]  # points
width  = 800  # screen x_size
height = 800  # screen y_size
seed(5)  # random generator initialization


def generate_points():
   while True:
      x=random()
      y=random()
      r=(x*x+y*y)
      if r>0.5 and r<1.0 :
         points.append([500*x+100, 500*y+100])
      if len(points)==1000: 
         break
   points.append([500+250, 50])  # isolated point top right


def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 0.0, 1.0)
    # Draw points
    glColor3f (1.0, 1.0, 1.0)
    glPointSize (3)
    glBegin(GL_POINTS)
    for p in points:
       glVertex2f (p [0], p [1])
    glEnd()
    glutSwapBuffers ()  # display

def reshape (wid, hgt):
    global width, height
    width = wid
    height = hgt
    glViewport( 0, 0, width, height )
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluOrtho2D (0, width, height, 0) # reshape

def main (argv=None):
    if argv is None:
       argv = sys.argv
    generate_points()
    glutInit(argv)
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize (width, height)
    glutInitWindowPosition (100, 100)
    glutCreateWindow ("Polygon, no CGAL")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc (reshape)
    display()
    glutMainLoop()
    return


if __name__=='__main__':
    sys.exit(main())