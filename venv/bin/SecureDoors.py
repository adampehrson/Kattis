a = int(input())
inside = []

for x in range(a):
    occasion = list(map(str, input().split()))
    out = ''
    if occasion[0] == 'entry':
        out = out + occasion[1] + ' entered'
        if occasion[1] in inside:
            out = out + ' (ANOMALY)'
        else:
            inside.append(occasion[1])
        print(out)

    if occasion[0] == 'exit':
        out = out + occasion[1] + ' exited'
        if occasion[1] not in inside:
            out = out + ' (ANOMALY)'
        else:
            inside.pop(inside.index(occasion[1]))
        print(out)

