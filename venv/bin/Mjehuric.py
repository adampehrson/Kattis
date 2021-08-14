def swap(sequence, a, b):
    if sequence[a] > sequence[b]:
        temp = sequence[a]
        sequence[a] = sequence[b]
        sequence[b] = temp

        print(str(sequence[0]) + " " + str(sequence[1]) + " " + str(sequence[2]) + " " + str(sequence[3]) + " " + str(sequence[4]))
    return sequence

sequence = list(map(int, input().split()))

while sequence != [1,2,3,4,5]:
    sequence = swap(sequence, 0, 1)
    sequence = swap(sequence, 1, 2)
    sequence = swap(sequence, 2, 3)
    sequence = swap(sequence, 3, 4)


