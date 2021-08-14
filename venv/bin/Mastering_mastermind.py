def helper(data, x):
    if data[1].count(x) < data[2].count(x):
        return data[1].count(x)
    else:
        return data[2].count(x)





data = input().split()




firstout = 0

total = dict()
for x in range(65, 91):
    total.update({chr(x): helper(data, chr(x))})


for x in range(len(data[1])):
    if data[1][x] == data[2][x]:
        firstout += 1
        if total[data[1][x]] > 0:
            total[data[1][x]] -= 1


print("{} {}".format(firstout, sum(total.values())))



