size = list(map(int, input().split()))
i = 0
horizontal = list()
smol = 'zzzzz'
while i < size[0]:
    horizontal.append(input())
    temp = horizontal[i].split('#')
    for x in temp:
        if len(x) > 1:
            if x < smol:
                smol = x
    i += 1
i = 0
vertical = list()
while i < size[1]:
    temp = ''
    for x in horizontal:
        temp = temp + x[i]
    vertical.append(temp)
    temp = vertical[i].split('#')
    for x in temp:
        if len(x) > 1:
            if x < smol:
                smol = x
    i += 1
print(smol)