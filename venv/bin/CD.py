import sys

while True:
    cds = list(map(int, sys.stdin.readline().split()))
    if cds[0] == 0 and cds[1] == 0:
        break

    i = 0
    jack = []
    jill = []
    while i < cds[0]:
        jack.append(int(sys.stdin.readline().strip()))
        i += 1

    i = 0
    while i < cds[1]:
        jill.append(int(sys.stdin.readline().strip()))
        i += 1

    pos1 = 0
    pos2 = 0
    out = 0
    while pos1 < len(jack) and pos2 < len(jill):
        if jack[pos1] < jill[pos2]:
            pos1 += 1
        elif jack[pos1] == jill[pos2]:
            pos1 += 1
            pos2 += 1
            out += 1
        elif jack[pos1] > jill[pos2]:
            pos2 += 1

    print(out)