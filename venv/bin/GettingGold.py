import sys
sys.setrecursionlimit(10000)

def changetofloor(dungeon, x, y):
    if len(dungeon[y]) > x:
        dungeon[y] = dungeon[y][:x] + '.' + dungeon[y][x + 1:]


def leavesquare(dungeon, x, y):
    if dungeon[y][x] == 'G':
        dungeon[y] = dungeon[y][:x] + '#' + dungeon[y][x+1:]
        return 1
    else:
        dungeon[y] = dungeon[y][:x] + '#' + dungeon[y][x+1:]
    return 0



def checktraps(dungeon, x, y):
    if dungeon[y - 1][x] == 'T':
        return 1
    if dungeon[y + 1][x] == 'T':
        return 1
    if dungeon[y][x - 1] == 'T':
        return 1
    if dungeon[y][x + 1] == 'T':
        return 1
    return 0


def movedown(dungeon, x, y):
    if dungeon[y + 1][x] == '.' or dungeon[y + 1][x] == 'G':
        return moves(dungeon, x, y + 1)
    else:
        return 0


def moveup(dungeon, x, y):
    if dungeon[y - 1][x] == '.' or dungeon[y - 1][x] == 'G':
        return moves(dungeon, x, y - 1)
    else:
        return 0


def moveright(dungeon, x, y):
    if dungeon[y][x + 1] == '.' or dungeon[y][x + 1] == 'G':
        return moves(dungeon, x + 1, y)
    else:
        return 0


def moveleft(dungeon, x, y):
    if dungeon[y][x - 1] == '.' or dungeon[y][x - 1] == 'G':
        return moves(dungeon, x - 1, y)
    else:
        return 0


def moves(dungeon, x, y):
    z = 0

    for w in dungeon:
        print(w)
    print()

    z = z + leavesquare(dungeon, x, y)

    if checktraps(dungeon, x, y) == 0:
        z = z + moveup(dungeon, x, y) + movedown(dungeon, x, y) + moveright(dungeon, x, y) + moveleft(dungeon, x, y)
    return z




size = list(map(int, input().split()))
dungeon1 = []

i = 0
while i < size[1] + 2:
    if i == 0:
        word = '##'
        for w in range(size[0]):
            word = word + '#'
        dungeon1.append(word)
    elif i == size[1] + 1:
        word = '##'
        for w in range(size[0]):
            word = word + '#'
        dungeon1.append(word)
    else:
        a = input()
        a = '#' + a + '#'
        dungeon1.append(a)
    i += 1


