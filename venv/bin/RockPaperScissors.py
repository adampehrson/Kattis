import sys

def movedown(dungeon, x, y, number, changeto):
    if dungeon[y + 1][x] == changeto:
        return 1
    return 0



def moveup(dungeon, x, y, number, changeto):
    if dungeon[y - 1][x] == changeto:
        return 1
    return 0



def moveright(dungeon, x, y, number, changeto):
    if dungeon[y][x + 1] == changeto:
        return 1
    return 0



def moveleft(dungeon, x, y, number, changeto):
    if dungeon[y][x - 1] == changeto:
        return 1
    return 0


def moves(dungeon, x, y, number, changeto):

    z = moveup(dungeon, x, y, number, changeto) + movedown(dungeon, x, y, number, changeto) + moveright(dungeon, x, y, number, changeto) + moveleft(dungeon, x, y, number, changeto)
    return z



tests = int(input())
for _ in range(tests):

    size = list(map(int, sys.stdin.readline().split()))
    binmap = []

    i = 0
    while i < size[0] + 2:
        temp = []
        if i == 0 or i == size[0] + 1:
            temp.append('#')
            for w in range(size[1]):
                temp.append('#')
            temp.append('#')
        else:
            a = sys.stdin.readline().strip()
            temp.append('#')
            for w in range(len(a)):
                temp.append(a[w])
            temp.append('#')
        binmap.append(temp)
        i += 1


    print(binmap)
    for __ in range(tests[2]):
        i = 0
        while i < len(binmap):
            e = 0
            while e < len(binmap[i]):
                if binmap[i][e] == 'R':
                    if moves(binmap, e, i, 'R', 'S') != 0
