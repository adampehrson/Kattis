class Grid:
    def __init__(self,xdim,ydim,grid):
        self.xdim = xdim
        self.ydim = ydim
        self.grid = grid


    def adjacent(self, pos):
        out = []
        if pos % self.xdim > 0:
            out.append(pos - 1)
        if (pos % self.xdim) + 1 < self.xdim:
            out.append(pos + 1)
        if pos // self.xdim > 0:
            out.append(pos - self.xdim)
        if (pos // self.xdim) + 1 < self.ydim:
            out.append(pos + self.xdim)
        return out



def propagation(mymap):
    out = []
    i = 0
    while i < len(mymap.grid):
        near = mymap.adjacent(i)
        for x in near:
            temp = change(mymap.grid[i], mymap.grid[x])
            if temp != mymap.grid[i]:
                out.append(temp)
                break

        i += 1
        if len(out) != i:
            out.append(mymap.grid[i-1])

    mymap.grid = out
    return mymap


def change(center,adjacent):
    if (adjacent + 1) % 3 == center:
        return adjacent
    return center





tests = int(input())

for a in range(tests):
    grid = []
    info = list(map(int, input().split()))
    for x in range(info[0]):
        temp = input()
        for y in temp:
            if y == "R":
                grid.append(0)
            if y == "S":
                grid.append(1)
            if y == "P":
                grid.append(2)

    mymap = Grid(info[1], info[0], grid)


    i = 0
    while i < info[2]:
        mymap = propagation(mymap)
        i += 1



    final = []
    i = 0
    while i < len(mymap.grid):
        temp = ""
        e = 0
        while e < mymap.xdim:
            y = mymap.grid[i + e]
            if y == 0:
                temp += "R"
            if y == 1:
                temp += "S"
            if y == 2:
                temp += "P"
            e += 1
        final.append(temp)
        i += mymap.xdim

    for x in final:
        print(x)
    print()

