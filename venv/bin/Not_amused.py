import sys

i = 1
while True:

    first = sys.stdin.readline().strip()
    if first == "":
        break

    if i != 1:
        print()

    mydict = dict()
    while True:
        current_line = sys.stdin.readline().split()
        if current_line[0] == "CLOSE":
            break
        if current_line[0] == "ENTER":
            if current_line[1] not in mydict:
                mydict.update({current_line[1]: [int(current_line[2]), 0]})
            else:
                mydict[current_line[1]][0] = int(current_line[2])
        elif current_line[0] == "EXIT":
            mydict[current_line[1]][1] += int(current_line[2]) - mydict[current_line[1]][0]


    print("Day {}".format(i))
    for y in sorted(mydict.keys()):
        temp = str(mydict[y][1]*0.1)
        temp = temp[:temp.index(".") + 2]
        print("{} ${}0".format(y, temp))


    i += 1


