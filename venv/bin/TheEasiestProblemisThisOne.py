while True:
    a = input()
    if a == '0':
        break
    i = 11
    tot1 = 0
    tot2 = 0
    for x in range(len(a)):
        tot1 = tot1 + int(a[x])

    while tot1 != tot2:
        tot2 = 0
        temp = str(i*int(a))
        for y in range(len(temp)):
            tot2 = tot2 + int(temp[y])
        i += 1

    print(i-1)