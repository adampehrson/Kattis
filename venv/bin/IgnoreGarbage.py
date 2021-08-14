import fileinput


def base7(x, lst, i):
    y = x
    if x >= 7**(i):
        i += 1
    elif 7**(i-1) <= x < 7**(i):
        i -= 1
        lst.append(x // 7**i)
        y = x % 7**i
    while i > 0:
        if y < 7**(i-1):
            lst.append(0)
            i -= 1
        else:
            break
    if y != 0:
        return base7(y, lst, i)


    return lst


i = 0
for line in fileinput.input():
    line = int(line)
    lst = list()
    output = base7(line, lst, 1)
    a = ''
    for z in output:
        a = a + str(z)
    a = a[::-1]
    x = a.count('5')
    a = a.replace('5', '8', x)
    x = a.count('3')
    a = a.replace('3', '5', x)
    x = a.count('4')
    a = a.replace('4', '9', x)

    print(a)

