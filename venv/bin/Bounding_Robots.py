while True:

    room = list(map(int, input().split()))
    if room[0] == 0 and room[1] == 0:
        break


    segments = int(input())
    actualpos = [0,0]
    expectedpos = [0,0]

    x = 0
    while x < segments:
        temp = input().split()
        temp[1] = int(temp[1])
        if temp[0] == "u":
            expectedpos[1] += temp[1]
            actualpos[1] += temp[1]
        elif temp[0] == "d":
            expectedpos[1] -= temp[1]
            actualpos[1] -= temp[1]
        elif temp[0] == "r":
            expectedpos[0] += temp[1]
            actualpos[0] += temp[1]
        elif temp[0] == "l":
            expectedpos[0] -= temp[1]
            actualpos[0] -= temp[1]
        if actualpos[0] >= room[0]:
            actualpos[0] = room[0] - 1
        if actualpos[0] < 0:
            actualpos[0] = 0
        if actualpos[1] >= room[1]:
            actualpos[1] = room[1] - 1
        if actualpos[1] < 0:
            actualpos[1] = 0


        x += 1

    print("Robot thinks " + str(expectedpos[0]) + " " + str(expectedpos[1]))

    print("Actually at " + str(actualpos[0]) + " " + str(actualpos[1]))
    print()