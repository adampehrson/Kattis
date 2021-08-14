import sys

sys.setrecursionlimit(10000000)


def leavesquare(dungeon, x, y, changeto):
    dungeon[y][x] = changeto


def movedown(dungeon, x, y, number, changeto):
    if dungeon[y + 1][x] == number:
        return moves(dungeon, x, y + 1, number, changeto)


def moveup(dungeon, x, y, number, changeto):
    if dungeon[y - 1][x] == number:
        return moves(dungeon, x, y - 1, number, changeto)



def moveright(dungeon, x, y, number, changeto):
    if dungeon[y][x + 1] == number:
        return moves(dungeon, x + 1, y, number, changeto)



def moveleft(dungeon, x, y, number, changeto):
    if dungeon[y][x - 1] == number:
        return moves(dungeon, x - 1, y, number, changeto)




def moves(dungeon, x, y, number, changeto):
    leavesquare(dungeon, x, y, changeto)
    moveup(dungeon, x, y, number, changeto)
    movedown(dungeon, x, y, number, changeto)
    moveright(dungeon, x, y, number, changeto)
    moveleft(dungeon, x, y, number, changeto)






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


i = 2
while True:
    e = 1
    amount = 0
    while e + 1 < len(binmap):
        if binmap[e].count('0') != 0:
            amount += 1
            moves(binmap, binmap[e].index('0'), e, '0', str(i))
            break
        e += 1
    if amount == 0:
        break
    i += 2




i = 3
while True:
    e = 0
    amount = 0
    while e < len(binmap):
        if binmap[e].count('1') != 0:
            amount += 1
            moves(binmap, binmap[e].index('1'), e, '1', str(i))
            break
        e += 1
    if amount == 0:
        break
    i += 2




tests = int(sys.stdin.readline())
i = 0
while i < tests:
    coords = list(map(int, sys.stdin.readline().split()))
    if binmap[coords[0]][coords[1]] == binmap[coords[2]][coords[3]]:
        if int(binmap[coords[0]][coords[1]]) % 2 == 0:
            print('binary')
        if int(binmap[coords[2]][coords[3]]) % 2 == 1:
            print('decimal')
    else:
        print('neither')
    i += 1
