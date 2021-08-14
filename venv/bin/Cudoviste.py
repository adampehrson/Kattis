tests = list(map(int, input().split()))
map = []
cars = [0, 0, 0, 0, 0]



i = 0
while i < tests[0]:
    map.append(input())
    i += 1

i = 0
while i + 1 < tests[0]:
    e = 0
    while e + 1 < tests[1]:
        templst = [map[i][e], map[i][e+1], map[i+1][e], map[i+1][e+1]]
        if templst.count('#') == 0:
            cars[templst.count('X')] += 1
        e += 1
    i += 1

print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print(cars[4])
