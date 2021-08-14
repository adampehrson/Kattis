import sys

i = 1
for line in sys.stdin:
    orbits = list(map(int, line.split()))
    mars = orbits[1]
    earth = orbits[0]
    days = 0

    while mars != 0 or earth != 0:
        days += 1
        mars = (mars + 1) % 687
        earth = (earth + 1) % 365

    print('Case ' + str(i) + ': ' + str(days))
    i += 1