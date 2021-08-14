parameters = list(map(int, input().split()))

i = 0
while i < parameters[0]:
    line = input()
    e = 0
    mod = ''
    while e < parameters[1]:
        mod = mod + line[e]*parameters[3]
        e += 1
    e = 0
    while e < parameters[2]:
        print(mod)
        e += 1
    i += 1