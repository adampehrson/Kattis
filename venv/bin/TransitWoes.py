
big = []


i = 0
while i < 4:
    big.append(list(map(int, input().split())))
    i += 1

time = big[0][0]

i = 0
while i < big[0][2]:
    time = time + big[1][i]
    if time % big[3][i] != 0:
        time = time - (time % big[3][i]) + big[3][i]
    time = time + big[2][i]
    i += 1


time = time + big[1][i]


if time <= big[0][1]:
    print('yes')
else:
    print('no')