"""Example of using lists in python."""

from random import *

numbers = []
seed(7)


def fill_numbers():
    """Create an array with 6 random numbers."""
    for i in range(6):
        n = random()
        numbers.append(n)

fill_numbers()
print "numbers", numbers
del numbers[0]
print "numbers", numbers
numbers.sort()
print "numbers", numbers
numbers.reverse()
print "numbers", numbers

for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1
# Equivalent to:
#   numbers = [x + 1 for x in numbers]

print "numbers", numbers

print "maximum", max(numbers)
print "minimum", min(numbers)

i = 0
while numbers[i] > 1.5:
    print numbers[i]
    i = i + 1
# Equivalent to:
#   print([x for x in numbers if x > 1.5])
