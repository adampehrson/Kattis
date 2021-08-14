import sys

while True:
    people = int(input())
    if people == 0:
        break
    mydict = dict()
    for x in range(people):
        person = input().split()
        for y in person[1:]:
            if y not in mydict:
                mydict.update({y: [person[0]]})
            else:
                mydict[y].append(person[0])
                mydict[y] = sorted(mydict[y])

    for x in sorted(mydict.keys()):
        out = x + " "
        for y in mydict[x]:
            out += y + " "
        print(out[:-1])