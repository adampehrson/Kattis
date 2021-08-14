from itertools import product
from sys import stdin


def get_adjacent_cells(grid, x_coord, y_coord):
    for x, y in [(x_coord+i, y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i**2 + j**2 < 2 and (i != 0 or j != 0)]:
        if (x, y) in grid and grid[(x, y)] is None:
            grid.update({(x, y): 1})
    return grid


data = list(map(int, stdin.readline().split()))
mydict = dict.fromkeys(list(product(range(data[1]), range(data[0]))))

for x in range(data[2]):
    temp = list(map(int, stdin.readline().split()))
    temp = {(temp[1] - 1, temp[0] - 1): 1}
    mydict.update(temp)

days = 1
while None in mydict.values():
    this_temp = [x for x in mydict if mydict[x] is not None]
    for x in this_temp:
        mydict = get_adjacent_cells(mydict, x[0], x[1])

    days += 1

print(days)
