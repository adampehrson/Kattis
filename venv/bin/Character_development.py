import math

a = int(input())

if a < 2:
    print(0)

else:
    temp = 1
    out = 0
    for x in range(2, a+1):
        temp = temp*x
        out += math.factorial(a) // (temp * math.factorial(a-x))
    print(out)
