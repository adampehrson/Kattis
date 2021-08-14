def checkmoves(karta, posx, posy):
    moves = 0
    if karta[posy][posx - 1] == 'o':
        if karta[posy][posx - 2] == 'o':
            moves += 1
    if karta[posy][posx + 1] == 'o':
        if karta[posy][posx + 2] == 'o':
            moves += 1
    if karta[posy - 1][posx] == 'o':
        if karta[posy - 2][posx] == 'o':
            moves += 1
    if karta[posy + 1][posx] == 'o':
        if karta[posy + 2][posx] == 'o':
            moves += 1
    return moves

karta = []
karta.append('         ')
i = 0
while i < 7:
    karta.append(' ' + input() + ' ')
    i += 1
karta.append('         ')



moves = 0
i = 1
while i < 8:
    e = 0
    while e < 8:
        if karta[i][e] == '.':
            moves = moves + checkmoves(karta, e, i)
        e += 1
    i += 1
print(moves)
