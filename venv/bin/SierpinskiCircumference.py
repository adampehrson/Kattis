import sys
e = 0
for line in sys.stdin:
    e += 1
    lst = [3.0, 1]
    x = 0
    while x < int(line):
        lst[0] = lst[0]*1.5
        if lst[0] >= 10:
            lst[1] += 1
            lst[0] = lst[0] / 10
        x += 1



    out = 'Case ' + str(e) + ': ' + str(lst[1])
    print(out)

