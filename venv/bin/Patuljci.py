numbers = []
for x in range(9):
    numbers.append(int(input()))
broken = []

i = 0
while i < 9:
    e = 0
    while e < 9:
        if e != i:
            j = 0
            total = 0
            while j < 9:
                if j != i and j != e:
                    total += numbers[j]
                j += 1
            if total == 100:
                broken.append(i)
                broken.append(e)
                break
        e += 1
    i += 1

q = 0
while q < 9:
    if q not in broken:
        print(numbers[q])
    q += 1