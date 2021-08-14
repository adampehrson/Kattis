amount = int(input())

bricks = list(map(int, input().split()))

out = 1

for x in range(1,len(bricks)):
    if bricks[x] > bricks[x-1]:
        out += 1


print(out)