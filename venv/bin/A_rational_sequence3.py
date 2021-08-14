tests = int(input())

for x in range(tests):
    data = list(map(int, input().split()))
    temp = bin(data[1])
    temp = temp[3:]

    out = [1, 1]
    for y in temp:
        if y == "0":
            out[1] = out[0] + out[1]
        else:
            out[0] = out[0] + out[1]


    print("{} {}/{}".format(x+1, out[0], out[1]))
