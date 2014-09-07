#!/usr/bin/env python

from fractions import *
from random import *
a = Fraction(24,10)
b = Fraction(24987654321345612349056,113570864213680646852690)
pi = Fraction.from_float(3.14159265358979)
c = Fraction.from_float(random())
d= Fraction.from_float(random())
tmp=(((a+b)*pi-c/d)**2)   
print tmp
print float(tmp)
