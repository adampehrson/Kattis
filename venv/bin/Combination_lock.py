import sys


def counter_clockwise(startvalue, endvalue):
    if startvalue >= endvalue:
        return startvalue - endvalue
    else:
        return 360 + startvalue - endvalue


def clockwise(startvalue, endvalue):
    if endvalue >= startvalue:
        return endvalue - startvalue
    else:
        return 360 + endvalue - startvalue




while True:
    data = list(map(int, input().split()))

    if data == [0,0,0,0]:
        break

    data = [9*x for x in data]

    total = 1080
    total += counter_clockwise(data[0], data[1])
    total += clockwise(data[1], data[2])
    total += counter_clockwise(data[2], data[3])
    print(total)
