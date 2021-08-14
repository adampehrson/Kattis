row = 0
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0

def revwhitep(lst):
    x = 1
    temp = list()
    while x < 9:
        for y in lst:
            if y[1] == str(x):
                temp.append(y)
        x += 1
    return temp

def revwhite(lst):
    x = 1
    temp = list()
    while x < 9:
        for y in lst:
            if y[2] == str(x):
                temp.append(y)
        x += 1
    return temp

def revblackp(lst):
    x = 8
    temp = list()
    while x > 0:
        for y in lst:
            if y[1] == str(x):
                temp.append(y)
        x -= 1
    return temp


def revblack(lst):
    x = 8
    temp = list()
    while x > 0:
        for y in lst:
            if y[2] == str(x):
                temp.append(y)
        x -= 1
    return temp



whitek = list()
whiteq = list()
whiter = list()
whiteb = list()
whiten = list()
whitep = list()
blackk = list()
blackq = list()
blackr = list()
blackb = list()
blackn = list()
blackp = list()
while i < 8:
    input()
    board = list(input().split('|'))
    e = 0
    while e < 8:
        if board[e+1][1] != '.':
            if board[e + 1][1] != ':':
                if board[e + 1][1].islower() == True:
                    piece = board[e + 1][1].capitalize() + column[e] + str(8-i)
                    if piece[0] == 'K':
                        blackk.append(piece)
                    if piece[0] == 'Q':
                        blackq.append(piece)
                    if piece[0] == 'R':
                        blackr.append(piece)
                    if piece[0] == 'B':
                        blackb.append(piece)
                    if piece[0] == 'N':
                        blackn.append(piece)
                    if piece[0] == 'P':
                        blackp.append(piece[1:])
                else:
                    piece = board[e + 1][1].capitalize() + column[e] + str(8 - i)
                    if piece[0] == 'K':
                        whitek.append(piece)
                    if piece[0] == 'Q':
                        whiteq.append(piece)
                    if piece[0] == 'R':
                        whiter.append(piece)
                    if piece[0] == 'B':
                        whiteb.append(piece)
                    if piece[0] == 'N':
                        whiten.append(piece)
                    if piece[0] == 'P':
                        whitep.append(piece[1:])
        e+=1
    i+=1

whiteK = revwhite(whitek)
whiteQ = revwhite(whiteq)
whiteR = revwhite(whiter)
whiteB = revwhite(whiteb)
whiteN = revwhite(whiten)
whiteP = revwhitep(whitep)



blackK = revblack(blackk)
blackQ = revblack(blackq)
blackR = revblack(blackr)
blackB = revblack(blackb)
blackN = revblack(blackn)
blackP = revblackp(blackp)

white = whiteK + whiteQ + whiteR + whiteB + whiteN + whiteP
black = blackK + blackQ + blackR + blackB + blackN + blackP





separ = ','
print('White: ' + separ.join(white))
print('Black: ' + separ.join(black))