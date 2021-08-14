lines = list(map(int, input().split()))[0]

dance = []
out = 1
for x in range(lines):
    dance.append(input()[1:-1])

for x in range(len(dance[0])):
    newmove = True
    for y in range(len(dance)):
        if dance[y][x] != "_":
            newmove = False
            break
    if newmove:
        out += 1

print(out)
