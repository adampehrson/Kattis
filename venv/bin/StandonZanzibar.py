cases = int(input())

i = 0
while i < cases:
    seq = list(map(int, input().split()))
    immigration = 0

    e = 0
    while e + 2 < len(seq):
        if seq[e]*2 < seq[e+1]:
            immigration = immigration + seq[e+1] - seq[e]*2
        e += 1
    print(immigration)
    i += 1
