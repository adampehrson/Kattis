import sys

tests = int(input())

for x in range(tests):
    sys.stdin.readline()
    monsters = sys.stdin.readline().split()
    godzilla = 0
    mechgodzilla = 0
    temp = list(map(int, sys.stdin.readline().split()))
    for y in temp:
        if y > godzilla:
            godzilla = y
    temp2 = list(map(int, sys.stdin.readline().split()))
    for w in temp2:
        if w > mechgodzilla:
            mechgodzilla = w
    if len(temp) == 0 and len(temp2) == 0:
        print('uncertain')
    elif mechgodzilla > godzilla:
        print('MechaGodzilla')
    elif godzilla >= mechgodzilla:
        print('Godzilla')