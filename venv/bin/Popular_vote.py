import sys

cases = int(input())

for x in range(cases):
    candidates = int(sys.stdin.readline())
    tot = 0
    highest = [0,-1]
    amounts = []
    for y in range(candidates):
        temp = int(sys.stdin.readline())
        tot += temp
        if temp > highest[0]:
            highest[0] = temp
            highest[1] = y+1
        elif temp == highest[0]:
            highest[1] = -1

    if highest[1] == -1:
        print("no winner")
    elif highest[0] > (tot // 2):
        print("majority winner {}".format(highest[1]))
    else:
        print("minority winner {}".format(highest[1]))
