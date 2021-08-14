cases = int(input())

i = 0
while i < cases:
    N = int(input())
    e = 1
    tot = 1
    while e <= N:
        tot = tot*e
        e += 1
    print(str(tot)[-1])
    i += 1
