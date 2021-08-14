from collections import Counter

info = list(map(int, input().split(' ')))
num = list(map(int, input().split(' ')))
output = ''
case5 = list()
def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i


if info[1] == 1:
    num = list(dict.fromkeys(num))
    num.sort()
    x = 0
    while x < len(num) - 1:
        y = x + 1
        if num[x] + num[-1] < 7777:
            y = len(num)
        if num[x] + num[x + 1] > 7777:
            y = len(num)
        while y < len(num):
            if num[x] + num[y] == 7777:
                output = 'Yes'
                x = len(num)
                y = len(num)
            y += 1
        x += 1
    if output == '':
        output = 'No'
    print(output)

if info[1] == 2:
    if len(num) == len(list(dict.fromkeys(num))):
        output = 'Unique'
    else:
        output = 'Contains duplicate'
    print(output)

if info[1] == 3:
    a, b = Counter(num).most_common(1)[0]
    if b > info[0] / 2:
        print(a)
    else:
        print(-1)

if info[1] == 4:
    num.sort()
    if int(info[0] % 2) == 1:
        output = num[(info[0] // 2)]
    else:
        output = str(num[int((info[0] - 1)/ 2)]) + ' ' + str(num[(int((info[0] - 1)/ 2)) + 1])
    print(output)

if info[1] == 5:

    arr1 = sorted(filter(lambda z: 99 < z < 1000, num))
    x = 0
    print(*arr1)




