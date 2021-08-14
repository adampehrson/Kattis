e = 1
while True:
    words = int(input())

    if words == 0:
        break
    start = []
    end = []
    i = 1
    while i <= words:
        start.append(input())
        i += 1
        if i > words:
            break
        end.insert(0, input())
        i += 1

    print('SET ' + str(e))
    for x in start:
        print(x)
    for y in end:
        print(y)

    e += 1