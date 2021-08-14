import sys
i = 1
for line in sys.stdin:

    line1 = list(map(int, line.split()))
    line2 = list(map(int, sys.stdin.readline().split()))

    a = line1[0]*line2[1] - line1[1]*line2[0]

    line1[0] = int(line1[0] / a)
    line1[1] = int(line1[1] / a)
    line2[0] = int(line2[0] / a)
    line2[1] = int(line2[1] / a)

    print('Case ' + str(i) + ':')
    print(str(line2[1]) + ' ' + str(-line1[1]))
    print(str(-line2[0]) + ' ' + str(line1[0]))
    sys.stdin.readline()

    i += 1