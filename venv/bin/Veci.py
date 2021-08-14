import itertools

number = input()

representation = []
for x in number:
    representation.append(int(x))

number = int(number)

all_possible = list(itertools.permutations(representation))


out = 10**6
i = 0
while i < len(all_possible):
    temp = ""
    for x in all_possible[i]:
        temp = temp + str(x)
    temp = int(temp)
    if number < temp < out:
        out = temp
    i += 1


if out < 10**6:
    print(out)

else:
    print(0)