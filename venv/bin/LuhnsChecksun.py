tests = int(input())

for i in range(tests):
    a = input()
    e = 1
    out = 0
    while e <= len(a):
        if e % 2 == 0:
            temp = int(a[-e])*2
            if temp >= 10:
                temp = str(temp)
                out = out + int(temp[0]) + int(temp[1])
            else:
                out = out + temp
        else:
            out = out + int(a[-e])
        e += 1
    if out % 10 == 0:
        print('PASS')
    else:
        print('FAIL')