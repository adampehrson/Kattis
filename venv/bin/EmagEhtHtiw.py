
white = input()[7:].split(',')

black = input()[7:].split(',')

board = [[], [], [], [], [], [], [], []]


i = 0
while i < len(board):
    e = 0
    while e < 8:
        board[i].append('')
        e += 1

    i += 1

i = 0
while i < len(white):
    if len(white[i]) == 0:
        break
    white[i] = white[i][:-2] + chr(ord(white[i][-2]) - 49) + str(int(white[i][-1]) - 1)
    if len(white[i]) == 3:
        board[int(white[i][-1])][int(white[i][-2])] = white[i][0]
    else:
        board[int(white[i][-1])][int(white[i][-2])] = 'P'
    i += 1

i = 0
while i < len(black):
    if len(black[i]) == 0:
        break
    black[i] = black[i][:-2] + chr(ord(black[i][-2]) - 49) + str(int(black[i][-1]) - 1)
    if len(black[i]) == 3:
        board[int(black[i][-1])][int(black[i][-2])] = black[i][0].lower()
    else:
        board[int(black[i][-1])][int(black[i][-2])] = 'p'
    i += 1


i = 0
while i < 8:
    e = 0
    while e < 8:
        if (i + e) % 2 == 1:
            board[i][e] = '.' + board[i][e] + '.'
            if len(board[i][e]) != 3:
                board[i][e] = board[i][e] + '.'
        else:
            board[i][e] = ':' + board[i][e] + ':'
            if len(board[i][e]) != 3:
                board[i][e] = board[i][e] + ':'
        e += 1
    i += 1


board = list(reversed(board))


i = 0
while i < 8:
    print('+---+---+---+---+---+---+---+---+')
    out = '|'
    e = 0
    while e < 8:
        out = out + board[i][e] + '|'
        e += 1
    print(out)
    i += 1

print('+---+---+---+---+---+---+---+---+')