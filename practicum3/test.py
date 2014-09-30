"""."""

def orientation(a, b, c):
    """Return true if the points a, b, c define a triangle counter clockwise."""
    return (
        (-a[1] * b[0] + a[0] * b[1] + a[1] * c[0]
         - b[1] * c[0] - a[0] * c[1] + b[0] * c[1]) < 0
    )

if __name__ == '__main__':
    p = [1, 3]
    q = [8, 4]
    e = [[4, 0], [4, 7]]
    print "Orientatie p met e\n"
    print(orientation(p, e[0], e[1]))
    print(orientation(p, e[1], e[0]))
    print(orientation(e[0], p, e[0]))
    print(orientation(e[0], e[1], p))
    print(orientation(e[1], e[0], p))
    print(orientation(e[1], p, e[0]))

    print "\n\nOrientatie p met e\n"
    print(orientation(q, e[0], e[1]))
    print(orientation(q, e[1], e[0]))
    print(orientation(e[0], q, e[0]))
    print(orientation(e[0], e[1], q))
    print(orientation(e[1], e[0], q))
    print(orientation(e[1], q, e[0]))
