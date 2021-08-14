cases = int(input())

for x in range(cases):
    data = list(map(int, input().split()))
    amount_in = 0
    ants = []
    while amount_in < data[1]:
        temp = list(map(int, input().split()))
        amount_in += len(temp)
        for z in temp:
            ants.append(z)
    earliest = 0
    latest = 0

    for y in ants:
        temp = y
        if temp > data[0] - y:
            temp = data[0] - y
        if temp > earliest:
            earliest = temp
        if data[0] - temp > latest:
            latest = data[0] - temp

    print("{} {}".format(earliest, latest))
