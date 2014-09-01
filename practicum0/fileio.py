"""Example of doing file IO in python."""

from random import seed, random
from string import split

n = int(raw_input("Please enter an integer: "))
fout = open("output.dat", "w")
seed(5)  # seed value of random generator
for i in range(n):
    x = random()
    y = random()
    print 'x y =', x, y
    fout.write(str(x) + " " + str(y) + "\n")
fout.close()

print ""

fin = open("output.dat", 'r')
for line in fin:
    b = split(line)
    x = (float(b[0]))
    y = (float(b[1]))
    print 'x y =', x, y
fin.close()

print ""

# Pythonic way according to Knupp:
with open('output.dat', 'r') as file_handle:
    for line in file_handle:
        b = split(line)
        x = (float(b[0]))
        y = (float(b[1]))
        print("x y = {x}, {y}".format(x=x, y=y))
