from sys import stdin

full_names = list()
duplicates = list()
while True:
    line = stdin.readline()
    if line == "":
        break

    line = line.split()
    if line[0] in [i[0] for i in full_names]:
        duplicates.append(line[0])

    full_names.append(line)


full_names.sort(key=lambda x: x[1] + x[0])


for x in full_names:
    if x[0] in duplicates:
        print("{} {}".format(x[0], x[1]))
    else:
        print(x[0])
