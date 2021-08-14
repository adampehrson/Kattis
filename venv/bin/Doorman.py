def change(mychar):
    if mychar == "W":
        return -1
    if mychar == "M":
        return 1


max_difference = int(input())

line = input()

mynewline = []

for x in line:
    if len(mynewline) == 0:
        mynewline.append(change(x))
    else:
        mynewline.append(change(x) + mynewline[-1])

broken = False
i = 0
for x in range(len(line)):
    if abs(mynewline[x]) > max_difference + 1:
        broken = True
        break
    i += 1

if broken:
    print(i-1)
else:
    print(i)
