import sys

i = 0
for line in sys.stdin:
    line.rstrip()
    i += 1
    a = list(map(int, line.split()))
    a = a[1:]
    a.sort()
    out = 'Case ' + str(i) + ': '
    out = out + str(a[0]) + ' ' + str(a[-1]) + ' ' + str(a[-1] - a[0])
    print(out)