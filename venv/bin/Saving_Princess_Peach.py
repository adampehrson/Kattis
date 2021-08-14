data = list(map(int, input().split()))

obstacles = set()
for x in range(data[0]):
    obstacles.add(x)

for x in range(data[1]):
    obstacles.discard(int(input()))

for x in obstacles:
    print(x)

print("Mario got {} of the dangerous obstacles.".format(data[0]-len(obstacles)))