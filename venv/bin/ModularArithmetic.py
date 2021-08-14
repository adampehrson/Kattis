import math

sad = 0
while sad == 0:
    run = input().split(" ")
    runs = [int(run[0]), int(run[1])]
    e = 0
    if runs[0] == 0:
        break
    while e < runs[1]:
        b = input().split(" ")
        if b[1] == '+':
            print((int(b[0]) + int(b[2])) % runs[0])
        elif b[1] == '-':
            print((int(b[0]) - int(b[2])) % runs[0])
        elif b[1] == '*':
            print((int(b[0]) * int(b[2])) % runs[0])
        elif b[1] == '/':
            if int(b[2]) == 0:
                print(-1)
            elif math.gcd(int(b[2]), runs[0]) != 1:
                print(-1)
            else:
                a = pow(int(b[2]), -1, mod=runs[0])
                print((int(b[0]) * a) % runs[0])
        e = e + 1
