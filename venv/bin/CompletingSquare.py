from math import sqrt


def distance(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def coordinates(near1,near2,opposite):
    out = []
    out.append(near1[0] + near2[0] - opposite[0])
    out.append(near1[1] + near2[1] - opposite[1])
    return out


x1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))
x3 = list(map(int, input().split()))

sides = []

sides.append(distance(x1,x2))
sides.append(distance(x1,x3))
sides.append(distance(x2,x3))

if sides[0] == sides[1]:
    print("{} {}".format(coordinates(x2,x3,x1)[0], coordinates(x2,x3,x1)[1]))
elif sides[1] == sides[2]:
    print("{} {}".format(coordinates(x2,x1,x3)[0], coordinates(x2,x1,x3)[1]))
else:
    print("{} {}".format(coordinates(x1,x3,x2)[0], coordinates(x1,x3,x2)[1]))
