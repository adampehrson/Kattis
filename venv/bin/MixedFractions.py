

i = 0
while i == 0:
    data = list(map(int, input().split()))
    if data[0] == 0 and data[1] == 0:
        break
    out = str(data[0] // data[1]) + ' '
    out = out + str(data[0] % data[1]) + ' / ' + str(data[1])
    print(out)
