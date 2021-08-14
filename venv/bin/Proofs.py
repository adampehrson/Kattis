import sys

cases = int(input())


myset = set()

i = 0
broken = False
for x in range(cases):
    i += 1
    line = sys.stdin.readline().split()
    if line[0] == "->":
        for y in line[1:]:
            myset.add(y)
    else:
        pos = line.index("->")
        for y in line[:pos]:
            if y not in myset:
                print(i)
                broken = True
                break
        myset.add(line[-1])

    if broken:
        break
if not broken:
    print("correct")