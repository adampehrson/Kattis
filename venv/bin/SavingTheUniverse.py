import sys
sys.setrecursionlimit(10000)


def checkswitch(engines, searches, pos):
    for x in engines:
        if x not in searches[pos:]:
            return 0
    return 1


def switch(engines, searches, pos):
    distance = []
    out = 0
    a = checkswitch(engines, searches, pos)
    out = out + a
    if a == 1:
        for x in engines:
            distance.append(searches[pos:].index(x))
        distance.sort()
        out = out + switch(engines, searches, pos + distance[-1])
    return out


cases = int(input())
i = 0
while i < cases:
    engines = []
    searches = []


    amounteng = int(input())
    e = 0
    while e < amounteng:
        engines.append(str(input()))
        e += 1

    amountsearch = int(input())
    e = 0
    while e < amountsearch:
        searches.append(str(input()))
        e += 1
    if amountsearch > 0:
        print('Case #' + str(i+1) + ': ' + str(switch(engines, searches, 0)))
    elif amountsearch == 0:
        print('Case #' + str(i + 1) + ': 0')
    i += 1