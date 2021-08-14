def width(a, ch1, ch2):
    i = 0
    value_toreturn = ""
    while i < a:
        if i % 2 == 0:
            value_toreturn = value_toreturn + ch1
        if i % 2 == 1:
            value_toreturn = value_toreturn + ch2
        i += 1
    return value_toreturn

crossword = list(map(int, input().split()))

frame = list(map(int, input().split()))

bredd = crossword[1]  + frame[1] + frame[2]
hojd = crossword[0] + frame[0] + frame[3]

out = []

for x in range(hojd):
    if x % 2 == 0:
        out.append(width(bredd, "#", "."))
    if x % 2 == 1:
        out.append(width(bredd, ".", "#"))


for x in range(frame[0], frame[0] + crossword[0]):
    temp = input()
    out[x] = out[x][0:frame[1]] + temp + out[x][frame[1] + crossword[1]:]


for x in out:
    print(x)