import sys
import itertools


words = []
while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    line = line.split()

    for x in line:
        if x not in words:
            words.append(x)


out = []

for x in words:
    for y in words:
        if y != x:
            if x + y not in out:
                out.append(x+y)

for x in sorted(out):
    print(x)