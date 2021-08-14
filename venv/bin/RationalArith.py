import math


def rationaladd(lst):
    if lst[0] == 0:
        return str(lst[3]) + ' / ' + str(lst[4])
    x = (lst[0]*lst[4] + lst[3]*lst[1]) // math.gcd(lst[1], lst[4])
    y = lst[1] * lst[4] // math.gcd(lst[1], lst[4])
    z = math.gcd(x, y)
    return str(x // z) + ' / ' + str(y // z)


def rationalsub(lst):
    if lst[0] == 0:
        return '-' + str(lst[3]) + ' / ' + str(lst[4])
    x = (lst[0]*lst[4] - lst[3]*lst[1]) // math.gcd(lst[1], lst[4])
    y = lst[1] * lst[4] // math.gcd(lst[1], lst[4])
    z = math.gcd(x, y)
    return str(x // z) + ' / ' + str(y // z)


def rationaldiv(lst):
    if lst[0] == 0:
        return '0 / 1'
    x = lst[0] * lst[4]
    y = lst[1] * lst[3]
    z = math.gcd(x, y)
    return str(x//z) + ' / ' + str(y//z)


def rationalmul(lst):
    if lst[0] == 0:
        return '0' + ' / ' + str(lst[1] * lst[4])
    x = lst[0] * lst[3]
    y = lst[1] * lst[4]
    z = math.gcd(x, y)
    return str(x//z) + ' / ' + str(y//z)


def rationalpos(data):
    arr = data.split()
    if int(arr[2]) < 0:
        arr[0] = int(arr[0]) * -1
        arr[2] = int(arr[2]) * -1
    return str(arr[0]) + ' ' + arr[1] + ' ' + str(arr[2])

tests = int(input())
i = 0

while i < tests:
    rip = input().split()
    num = [int(rip[0]), int(rip[1]), rip[2], int(rip[3]), int(rip[4])]
    if num[2] == '+':
        print(rationalpos(rationaladd(num)))
    if num[2] == '-':
        print(rationalpos(rationalsub(num)))
    if num[2] == '/':
        print(rationalpos(rationaldiv(num)))
    if num[2] == '*':
        print(rationalpos(rationalmul(num)))
    i+=1

