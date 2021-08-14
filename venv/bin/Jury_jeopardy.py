def moving(direction, position):
    if direction == 0:
        return [0, 1]
    elif direction == 1:
        return [1, 0]
    elif direction == 2:
        return [0, - 1]
    else:
        return [-1, 0]





cases = int(input())
print(cases)
for x in range(cases):

    currentpos = [0, 0]
    currentdir = 1
    spaces = []

    movement = input()
    for y in [movement[x] for x in range(len(movement))]:
        if y == "L":
            currentdir -= 1
            currentdir = currentdir % 4
        elif y == "R":
            currentdir += 1
            currentdir = currentdir % 4
        elif y == "B":
            currentdir += 2
            currentdir = currentdir % 4

        temp = moving(currentdir, currentpos)
        i = 0
        for a in temp:
            currentpos[i] += a
            i += 1
        if [currentpos[0], currentpos[1]] not in spaces:
            spaces.append((currentpos[0], currentpos[1]))

    spaces.sort()
    xmax = sorted(spaces)[-1][0]
    ymin = sorted([x[1] for x in spaces])[0]
    ymax = sorted([x[1] for x in spaces])[-1]

    out = []
    for ycoord in range(ymin, ymax + 1):
        temp = ""
        for xcoord in range(xmax + 1):
            if (xcoord, ycoord) not in spaces:
                temp += "#"
            else:
                temp += "."
        out.append(temp + "#")

    print("{} {}".format(len(out) + 2, len(out[0])))
    print("#"*len(out[0]))
    for line in out[::-1]:
        print(line)
    print("#"*len(out[0]))

