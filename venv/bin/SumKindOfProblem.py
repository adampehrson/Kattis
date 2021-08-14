tests = int(input())

for x in range(tests):
    case = list(map(int, input().split()))
    out = str(case[0]) + ' '
    temp = 0
    for i in range(case[1] + 1):
        temp = temp + i
    out = out + str(temp) + ' '
    temp = 0
    w = 0
    while w < case[1]:
        temp = temp + 2*w + 1
        w += 1
    w = 0
    out = out + str(temp) + ' '
    temp = 0
    while w <= case[1]:
        temp = temp + 2*w
        w+= 1
    out = out + str(temp) + ' '
    print(out)
