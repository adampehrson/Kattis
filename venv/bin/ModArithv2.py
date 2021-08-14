import math


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m


def modadd(a, b, mod):
    return (a + b) % mod


def modsub(a, b, mod):
    return (a - b) % mod


def modmul(a, b, mod):
    return (a * b) % mod


sad = 0
while sad == 0:
    run = input().split()
    runs = [int(run[0]), int(run[1])]
    if runs[0] == 0:
        sad = 1
    e = 0
    if runs[1] != 0:
        while e < runs[1]:
            temp = input().split()
            arr = [int(temp[0]), temp[1], int(temp[2])]
            if temp[1] == '-':
                print(modsub(arr[0], arr[2], runs[0]))
            if temp[1] == '+':
                print(modadd(arr[0], arr[2], runs[0]))
            if temp[1] == '*':
                print(modmul(arr[0], arr[2], runs[0]))
            if temp[1] == '/':
                x = modinv(arr[2], runs[0])
                if x == -1:
                    print(x)
                else:
                    print(arr[0]* x % runs[0])
            e = e + 1
