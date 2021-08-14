cases = int(input())

i = 0
while i < cases:
    amount = int(input())
    guests = list(map(int, input().split()))
    guests.sort()
    out = 'Case #' + str(i+1) + ': '
    e = 0
    while e < amount:
        if e == amount - 1:
            out = out + str(guests[e])
            break
        if guests[e] != guests[e+1]:
            out = out + str(guests[e])
            break
        e += 2
    print(out)
    i += 1