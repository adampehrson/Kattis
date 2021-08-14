students = int(input())

mydict = dict()

for x in range(students):
    temp = list(map(int, input().split()))
    temp.sort()
    newtemp = ""
    for x in temp:
        newtemp = newtemp + str(x) + " "

    if newtemp not in mydict:
        mydict[newtemp] = 1

    else:
        mydict[newtemp] += 1



out = 0
maximum = 0
for x in mydict.values():
    if x > maximum:
        out = x
        maximum = x
    elif x == maximum:
        out += x


print(out)