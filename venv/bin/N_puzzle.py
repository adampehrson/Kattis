from itertools import product

mydict = dict()

for x in range(4):
    for y in range(4):
        if y == 3 and x == 3:
            mydict.update({".": (x, y)})
        else:
            mydict.update({chr(65 + 4 * x + y): (x, y)})



out = 0
for x in range(4):
    line = input()
    for y in range(len(line)):
        if line[y] != ".":
            temp = mydict[line[y]]
            out += abs(x - temp[0]) + abs(y - temp[1])

print(out)