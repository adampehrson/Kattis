cases = int(input())

for x in range(cases):
    sequence = list(map(int, input().split()))[1:]
    difference = sequence[1] - sequence[0]
    i = 0
    arithmetic = True
    while i in range(len(sequence) - 1):
        if difference + sequence[i] != sequence[i+1]:
            arithmetic = False
            break
        i += 1
    sequence = sorted(sequence)
    difference = sequence[1] - sequence[0]
    permuted_arithmetic = True
    while i in range(len(sequence) - 1):
        if difference + sequence[i] != sequence[i+1]:
            permuted_arithmetic = False
            break
        i += 1
    if arithmetic:
        print("arithmetic")
    elif permuted_arithmetic:
        print("permuted arithmetic")
    else:
        print("non-arithmetic")
