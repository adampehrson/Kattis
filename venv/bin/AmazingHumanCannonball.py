import math

tests = int(input())

i = 0
while i < tests:
    lst = list(map(float, input().split()))
    v = lst[0]
    angle = math.pi*lst[1]/180
    x = lst[2]
    h1 = lst[3]
    h2 = lst[4]
    t = x / (v * math.cos(angle))
    y = (v * t * math.sin(angle)) - ((9.81 * (t*t)) / 2)
    if h1 + 1 <= y <= h2 - 1:
        print('Safe')
    else:
        print('Not Safe')
    i += 1