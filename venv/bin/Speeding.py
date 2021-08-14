photos = int(input())


speeds = []
previous = list(map(int, input().split()))

for x in range(photos - 1):
    current = list(map(int, input().split()))

    speeds.append((current[1]-previous[1]) / (current[0]- previous[0]))
    previous = current

speeds.sort()
print(int(speeds[-1]))


