while True:
    hydra = list(map(int, input().split()))
    if hydra == [0, 0]:
        break

    temp = hydra[1]
    moves = 0
    while hydra[1] > 0:
        if hydra[1] > 1:
            hydra[1] -= 2
            hydra[0] += 1
            moves += 1
        elif hydra[1] == 1:
            hydra[1] += 1
            moves += 1

    while hydra[0] > 0:
        if hydra[0] > 1:
            hydra[0] -= 2
            moves += 1
        elif hydra[0] == 1:
            if temp != 0:
                hydra[0] = 0
                moves += 4
    print(moves)

