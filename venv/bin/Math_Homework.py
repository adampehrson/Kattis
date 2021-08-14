def not_recursive(animals, total):
    possible = []
    i = 0
    while animals[0]*i <= total:
        e = 0
        while animals[1]*e <= total:
            w = 0
            while animals[2]*w <= total:
                if animals[0]*i + animals[1]*e + animals[2]*w == total:
                    possible.append("{} {} {}".format(i, e, w))
                w += 1
            e += 1
        i += 1
    return possible

data = list(map(int, input().split()))

out = not_recursive(data[:3], data[3])

if len(out) == 0:
    print("impossible")
else:
    for x in out:
        print(x)