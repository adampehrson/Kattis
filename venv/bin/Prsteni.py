import math

a = int(input())
b = list(map(int, input().split(' ')))
i = 1
while i < a:
    temp = b[0] / math.gcd(b[0], b[i])
    b[i] = b[i] / math.gcd(b[0], b[i])
    print(str(int((temp))) + '/' + str(int((b[i]))))
    i += 1




