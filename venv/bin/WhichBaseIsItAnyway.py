def base(a, b):
    out = 0
    i = 1
    while i <= len(a):
        out = out + int(a[-i])*(b**(i-1))
        i += 1
    return out



tests = int(input())
w = 0
while w < tests:

    num = input().split()
    out = num[0] + ' '
    i = 0
    par = False
    while i < len(num[1]):
        if num[1][i] == '9' or num[1][i] == '8':
            par = True
        i += 1
    if not par:
        out = out + str(base(num[1], 8)) + ' '
    if par:
        out = out + '0 '
    out = out + str(int(num[1])) + ' '
    out = out + str(base(num[1], 16))
    print(out)
    w += 1

