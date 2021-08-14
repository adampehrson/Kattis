import sys

amount = int(input())

taken = []

for x in range(amount):
    taken.append(sys.stdin.readline().strip())


taken = list(set(taken))
mydict = dict()
for x in taken:
    temp = x.split()[2]
    if temp in mydict:
        mydict[temp] += 1
    else:
        mydict.update({temp: 1})

for x in sorted(mydict.keys()):
    print("{} {}".format(x, mydict[x]))
