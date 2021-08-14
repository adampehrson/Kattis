group_size = int(input())
rolls = list(map(int, input().split()))

mydict = dict()

i = 0
for x in rolls:
    if x in mydict:
        mydict[x].append(i)
    else:
        mydict.update({x: [i]})
    i += 1

out = -1
for x in reversed(sorted(mydict.keys())):
    if len(mydict[x]) == 1:
        out = mydict[x][0]
        break

if out == -1:
    print("none")
else:
    print(out+1)