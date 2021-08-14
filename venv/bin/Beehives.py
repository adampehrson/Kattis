while True:

    data = input().split()

    distance = float(data[0])
    amount = int(data[1])
    if amount == 0:
        break

    hives = []
    for x in range(amount):
        hives.append(list(map(float, input().split())))

    sour = 0

    for x in hives:
        for y in hives:
            if y != x:
                temp = (x[0]-y[0])**2 + (x[1] - y[1])**2
                if temp <= distance**2:
                    sour += 1
                    break


    print("{} sour, {} sweet".format(sour, amount-sour))