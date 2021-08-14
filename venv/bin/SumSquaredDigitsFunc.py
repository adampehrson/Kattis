cases = int(input())

i = 0
while i < cases:
    case = list(map(int, input().split()))
    base = case[1]
    n = case[2]
    digits = 0
    out = 0

    while base**digits <= n:
        digits += 1

    while n > 0:
        out = out + (n // base**digits) ** 2
        n = n - (n // base**digits) * (base**digits)
        digits -= 1
    print(str(case[0]) + ' ' + str(out))

    i += 1