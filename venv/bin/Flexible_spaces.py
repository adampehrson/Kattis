data = list(map(int, input().split()))
partitions = list(map(int, input().split()))
partitions.insert(0, 0)
partitions.append(data[0])

possible = []
for x in partitions:
    for y in partitions:
        if x != y:
            if abs(x - y) not in possible:
                possible.append(abs(x-y))


out = ""
for x in sorted(possible):
    out += str(x) + " "
print(out[:-1])