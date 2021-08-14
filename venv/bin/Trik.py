moves = input()
cups = ['ball', 0, 0]


i = 0
while i < len(moves):
    a = cups[0]
    b = cups[1]
    c = cups[2]
    if moves[i] == 'A':
        cups[0] = b
        cups[1] = a
    if moves[i] == 'B':
        cups[1] = c
        cups[2] = b
    if moves[i] == 'C':
        cups[0] = c
        cups[2] = a
    i += 1
print(cups.index('ball') + 1)

