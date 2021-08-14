cards = input()

P = []
K = []
H = []
T = []
broken = False
i = 0
while i < len(cards):
    if cards[i] == 'P':
        temp = cards[i+1] + cards[i+2]
        if P.count(temp) != 0:
            print('GRESKA')
            broken = True
            break
        P.append(cards[i+1] + cards[i+2])
    if cards[i] == 'K':
        temp = cards[i + 1] + cards[i + 2]
        if K.count(temp) != 0:
            print('GRESKA')
            broken = True
            break
        K.append(cards[i+1] + cards[i+2])
    if cards[i] == 'H':
        temp = cards[i + 1] + cards[i + 2]
        if H.count(temp) != 0:
            print('GRESKA')
            broken = True
            break
        H.append(cards[i+1] + cards[i+2])
    if cards[i] == 'T':
        temp = cards[i + 1] + cards[i + 2]
        if T.count(temp) != 0:
            print('GRESKA')
            broken = True
            break
        T.append(cards[i+1] + cards[i+2])
    i += 3

if not broken:
    out = str(13 - len(P)) + ' '
    out = out + str(13 - len(K)) + ' '
    out = out + str(13 - len(H)) + ' '
    out = out + str(13 - len(T))
    print(out)