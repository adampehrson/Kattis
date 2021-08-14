


def grade(a):
    y = list(map(int, a.split(' ')))
    x = 0
    for i in y:
        x = x + i
    return x


e = 0
z = list()
z.append(0)
z.append(0)
result = 0
while e < 5:
    b = input()
    result = grade(b)
    if result > z[1]:
        z[0] = e + 1
        z[1] = result
    e += 1

print(str(z[0]) + ' ' + str(z[1]))


