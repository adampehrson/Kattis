tests = int(input())


i = 0
while i < tests:
    a = int(input())
    if a >= 2:
        red = []
        blue = []
        out = 0
        strings = list(map(str, input().split()))
        for x in strings:
            if x[-1] == 'R':
                red.append(int(x[:-1]))
            elif x[-1] == 'B':
                blue.append(int(x[:-1]))
        red.sort()
        red.reverse()
        blue.sort()
        blue.reverse()
        usable = min(len(red), len(blue))
        if usable == 0:
            out = 0
        else:
            for x in range(0, usable):
                out += int(red[x]) + int(blue[x]) - 2


        print('Case #' + str(i+1) + ': ' + str(out))
    else:
        input()
        print('Case #' + str(i + 1) + ': ' + str(0))
    i += 1
