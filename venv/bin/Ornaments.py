from math import pi
from math import sqrt

while True:
    data = list(map(int, input().split()))
    if data == [0, 0, 0]:
        break

    rope = pi*data[0]
    print(rope)
    rope += 2 * (sqrt(data[0]**2 + data[1]**2))
    print(rope)
    rope = rope*(1+data[2]/100)
    print(rope)
    print()
