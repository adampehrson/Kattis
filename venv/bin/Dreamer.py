import datetime
import itertools


cases = int(input())

for x in range(cases):
    mydate = "".join(input().split())
    mylist = []
    for y in mydate:
        mylist.append(int(y))
    mydate = mylist
    possibilities = list(itertools.permutations(mydate))
    possibilities = set(possibilities)
    smallest_possible = datetime.datetime(9999, 12, 31)
    total = 0
    for y in possibilities:
        if int(str(y[0]) + str(y[1]) + str(y[2]) + str(y[3])) >= 2000:
            try:
                temp = datetime.datetime(int(str(y[0]) + str(y[1]) + str(y[2]) + str(y[3])), int(str(y[4]) + str(y[5])), int(str(y[6]) + str(y[7])))
                total += 1
            except ValueError:
                temp = datetime.datetime(9999,12,31)

            if temp < smallest_possible:
                smallest_possible = temp


    if smallest_possible != datetime.datetime(9999, 12, 31):
        temp1 = str(smallest_possible.day)
        temp2 = str(smallest_possible.month)
        if len(temp1) == 1:
            temp1 = "0" + temp1
        if len(temp2) == 1:
            temp2 = "0" + temp2

        print("{} {} {} {}".format(total, temp1, temp2, smallest_possible.year))
    else:
        print(total)



