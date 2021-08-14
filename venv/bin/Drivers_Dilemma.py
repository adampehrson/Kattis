data = input().split()
capacity = float(data[0])
leak_rate = float(data[1])
distance = float(data[2])

speeds = []

for x in range(6):
    temp = input().split()
    temp2 = [float(temp[0]), float(temp[1])]
    speeds.append(temp2)

out = 0
for x in speeds:
    time = distance / x[0]
    if time*leak_rate + distance / x[1] < capacity / 2:
        if out < x[0]:
            out = x[0]

if out > 0:
    print("YES {}".format(int(out)))
else:
    print("NO")


