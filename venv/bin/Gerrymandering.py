tests = list(map(int, input().split()))
districts = []
i = 0
while i < tests[1]:
    districts.append([])
    districts[i].append(0)
    districts[i].append(0)
    districts[i].append(0)
    i += 1

i = 0
while i < tests[0]:
    precinct = list(map(int, input().split()))
    districts[precinct[0]-1][0] += precinct[1]
    districts[precinct[0]-1][1] = districts[precinct[0]-1][1] + precinct[2]
    districts[precinct[0]-1][2] = districts[precinct[0]-1][2] + precinct[1] + precinct[2]
    i += 1

wasted = [0,0,0]

for x in districts:
    if x[0] > x[1]:
        a = x[2] // 2
        wasted[0] += x[0] - a - 1
        wasted[1] += x[1]
        wasted[2] += x[0] + x[1]
        print('A ' + str(x[0] - a - 1) + ' ' + str(x[1]))
    else:
        a = x[2] // 2
        wasted[0] += x[0]
        wasted[1] += x[1] - a - 1
        wasted[2] += x[0] + x[1]
        print('B ' + str(x[0]) + ' ' + str(x[1] - a - 1))

if wasted[0] > wasted[1]:
    print((wasted[0] - wasted[1]) / wasted[2])
else:
    print((wasted[1] - wasted[0]) / wasted[2])