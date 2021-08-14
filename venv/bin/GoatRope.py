from math import sqrt

a = list(map(int, input().split()))

goat = [a[0], a[1]]
bottomleft = [a[2], a[3]]
topright = [a[4], a[5]]
dist = 0


if goat[0] < bottomleft[0]:
    dist = (bottomleft[0] - goat[0])**2

if goat[1] < bottomleft[1]:
    dist = dist + (bottomleft[1] - goat[1]) ** 2

if goat[0] > topright[0]:
    dist = dist + (goat[0] - topright[0])**2

if goat[1] > topright[1]:
    dist = dist + (goat[1] - topright[1]) ** 2

print(sqrt(dist))
