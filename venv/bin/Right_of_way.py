mydict = {
    "South": 0,
    "West": 1,
    "North": 2,
    "East": 3
}

data = input().split()

for x in range(len(data)):
    data[x] = mydict[data[x]]



if (data[0] + 2) % 4 == data[1] and (data[2] + 1) % 4 == data[0]:
    print("Yes")

elif (data[0] + 1) % 4 == data[1]:
    if (data[0] - 1) % 4 == data[2] or (data[0] + 2) % 4 == data[2]:
        print("Yes")
    else:
        print("No")
else:
    print("No")