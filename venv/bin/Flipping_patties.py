def changedict(a, thedict):
    if a in thedict:
        thedict[a] += 1
    else:
        thedict.update({a: 1})
    return thedict

orders = int(input())

mydict = dict()

for x in range(orders):
    neworder = list(map(int, input().split()))
    mydict = changedict(neworder[1], mydict)
    mydict = changedict(neworder[1] - neworder[0], mydict)
    mydict = changedict(neworder[1] - 2*neworder[0], mydict)

out = 0
for x in mydict.values():
    if (x + 1) // 2 > out:
        out = (x + 1) // 2
print(out)
