import math

while True:
    d, v = map(int, input().split())
    if d == 0 and v == 0:
        break
    a = pow((pow(d, 3) * math.pi / 6 - v) / (math.pi / 6), 1.0/3)
    print(a)

