pos = list(map(int, input().split()))

if pos[1] - pos[0] > pos[2] - pos[1]:
    print(pos[1] - pos[0] - 1)
else:
    print(pos[2] - pos[1] - 1)