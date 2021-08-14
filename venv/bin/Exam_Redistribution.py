rooms = int(input())

sizes = list(map(int, input().split()))

sugoi = []

i = 0
while i < len(sizes):
    sugoi.append((i+1, sizes[i]))
    i += 1


sugoi.sort(key=lambda x: x[1])
sugoi.reverse()


total = 0
for pair in sugoi:
   total += pair[1]


if sugoi[0][1] > total - sugoi[0][1]:
    print("impossible")
else:
    out = ""

    for x in sugoi:
        out = out + str(x[0]) + " "
    print(out[:-1])