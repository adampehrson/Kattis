import sys

while True:
    case = sys.stdin.readline()
    if case == "":
        break
    mydict = dict()

    for x in range(int(case)):
        intdict = input()
        temp = intdict.split()
        time = list(map(int, temp[0].split(":")))
        time.append(temp[1])
        normal_rep = 0
        if time[0] == 12:
            time[0] = 0
        normal_rep += 60*time[0] + time[1]

        if time[2] == "p.m.":
            normal_rep += 12*60

        if normal_rep not in mydict:

            mydict.update({normal_rep: [intdict, 1]})
        else:
            mydict[normal_rep][-1] += 1

    for x in sorted(mydict.keys()):
        for y in range(mydict[x][-1]):
            print(mydict[x][0])

    print()