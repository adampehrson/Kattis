while True:
    amount = int(input())
    if amount == -1:
        break

    vertices = []
    i = 0
    while i < amount:
        temp = list(map(int, input().split()))
        vertices.append(temp)
        i += 1

    out = []
    for x in range(len(vertices)):
        vertice_strong = False
        for y in range(len(vertices)):
            if vertices[x][y] == 1:
                for z in range(len(vertices)):
                    if vertices[y][z] == 1 and vertices[x][z] == 1:
                        vertice_strong = True
        if not vertice_strong:
            out.append(x)
    mystr = ""
    for x in out:
        mystr = mystr + str(x) + " "
    print(mystr[:-1])

