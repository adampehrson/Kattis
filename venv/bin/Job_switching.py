friends_amount = int(input())

positions = list(map(int, input().split()))






swaps = 0
for x in range(len(positions)):
    if positions[x] != x + 1:
        pos = positions.index(x+1)
        value = positions[pos]
        positions[pos] = positions[x]
        positions[x] = value
        swaps += 1
print(swaps)

