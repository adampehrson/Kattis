import sys
sys.setrecursionlimit(100000)



def makedark(stars, x, y):
    stars[y] = stars[y][:x] + '#' + stars[y][x+1:]
    checkadjacent(stars, x, y)



def checkadjacent(stars, x, y):
    if stars[y][x-1] == '-':
        makedark(stars, x - 1, y)
    if stars[y][x+1] == '-':
        makedark(stars, x + 1, y)
    if stars[y+1][x] == '-':
        makedark(stars, x, y+1)
    if stars[y-1][x] == '-':
        makedark(stars, x, y-1)
    return 1


w = 1
for line in sys.stdin:
    size = list(map(int, line.split()))
    stars = []
    out = 0
    empty = ''
    i = 0
    while i < size[1] + 2:
        empty = empty + '#'
        i += 1
    stars.append(empty)
    i = 0
    while i < size[0]:
        stars.append('#' + input() + '#')
        i += 1
    stars.append(empty)

    size[0] = len(stars)
    size[1] = len(stars[0])

    i = 0
    while i < size[0]:
        e = 0
        while e < size[1]:
            if stars[i][e] == '-':
                out += 1
                makedark(stars, e, i)
                checkadjacent(stars, e, i)
            e += 1
        i += 1

    print('Case ' + str(w) + ': ' + str(out))
    w += 1