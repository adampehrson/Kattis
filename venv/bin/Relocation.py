a = list(map(int, input().split()))
b = list(map(int, input().split()))
spots = []

for i in range(a[0]):
    spots.append(b[i])

i = 0
while i < a[1]:
    op = list(map(int, input().split()))
    if op[0] == 1:
        spots[op[1] - 1] = op[2]
    if op[0] == 2:
        out = spots[op[1] - 1] - spots[op[2] - 1]
        if out < 0:
            out = out*-1
        print(out)

    i += 1

