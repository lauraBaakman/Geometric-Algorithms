#!/usr/bin/env python

import random
import string

n = int(raw_input("Please enter an integer: "))
fout = open("output.dat", "w")
random.seed(5)  # seed value of random generator
for i in range(n):
  x=random.random()
  y=random.random()
  print 'x y =', x , y
  fout.write(str(x) + " " + str(y)  + "\n")
fout.close()
print ""
fin=open("output.dat",'r')
for line in fin:
   b=string.split(line)
   x=(float(b[0]))
   y=(float(b[1]))
   print 'x y =', x , y
fin.close()
 