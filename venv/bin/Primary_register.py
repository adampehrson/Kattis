total = 9699689
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

data = list(map(int, input().split()))

i = 0
while i < len(data):
    e = 0
    factor = 1
    while e < i:
        factor = factor*numbers[e]
        e += 1
    total = total - data[i]*factor
    i += 1

print(total)
