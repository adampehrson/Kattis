import math


tests = int(input())


for x in range(tests):
    data = list(map(int, input().split()))
    sides = data[0]
    length = data[1]
    area = sides*length*length / (4 * math.tan(math.pi/sides))

    initial = data[0] * data[1]
    increase = data[2] * data[3]
    print(area + initial * increase + increase * increase * math.pi)

