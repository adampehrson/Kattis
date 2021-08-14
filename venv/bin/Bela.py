
info = input().split(' ')
i = 0
score = 0
while i < 4*int(info[0]):
    card = input()
    if card[0] == 'A':
        score = score + 11
    if card[0] == 'K':
        score = score + 4
    if card[0] == 'Q':
        score = score + 3
    if card[0] == 'T':
        score = score + 10
    if card[0] == 'J':
        if info[1] == card[1]:
            score = score + 20
        else:
            score = score + 2
    if card[0] == '9':
        if info[1] == card[1]:
            score = score + 14
    i += 1

print(score)
