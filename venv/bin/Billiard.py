import math

a = 0
while a == 0:
    out = ''
    num = list(map(int, input().split(' ')))
    if sum(num) == 0:
        break
    l1 = num[0]*num[3]
    l2 = num[1]*num[4]
    temp = math.atan(l2/l1)
    out = str(round(180*temp/math.pi, 2))
    if out[::-1].find('.') == 1:
        out = out + '0'
    out = out + ' '
    dist = math.sqrt(l1*l1 + l2*l2)
    out = out + str(round(dist/num[2], 2))
    if out[::-1].find('.') == 1:
        out = out + '0'
    print(out)

