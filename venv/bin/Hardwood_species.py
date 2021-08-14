import sys


mydict = dict()
i = 0
while True:
    tree = sys.stdin.readline().strip()
    if tree == "":
        break
    i += 1
    if tree not in mydict:
        mydict.update({tree: 1})
    else:
        mydict[tree] += 1

    


for x in sorted(mydict.keys()):
    print("{} {}".format(x, 100*mydict[x]/i))
