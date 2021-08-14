cases = int(input())

for x in range(cases):
    scenario = list(map(int, input().split()))

    data = []
    for y in range(scenario[0]):
        data.append(input())

    out = ""

    for z in range(scenario[1]):
        temp = 0
        for w in range(scenario[0]):
            temp += int(data[w][z])
        if temp*2 > scenario[0]:
            out = out + "1"
        else:
            out = out + "0"
    print(out)