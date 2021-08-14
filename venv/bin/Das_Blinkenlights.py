data = list(map(int, input().split()))

factor = 1
i = 2
while i <= data[0] and i <= data[1]:
    if data[0] % i == 0 and data[1] % i == 0:
        data[0] = data[0] // i
        data[1] = data[1] // i
        factor = factor*i
        i = 2
    else:
        i += 1

if data[0]*data[1]*factor <= data[2]:
    print("yes")
else:
    print("no")