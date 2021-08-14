

data = list(map(int, input().split()))
numbers = list(map(int, input().split()))

mydict = dict()

i = 0
maxappearance = 1
for x in numbers:
    if x not in mydict:
        mydict.update({x: [x, 1, i]})
    else:
        mydict[x][1] += 1
        if mydict[x][1] > maxappearance:
            maxappearance = mydict[x][1]
    i += 1

out = sorted(mydict.values(), key= lambda x: (maxappearance - x[1], x[2]))

finalout = ""
for x in out:
    for y in range(x[1]):
        finalout += str(x[0]) + " "
print(finalout)