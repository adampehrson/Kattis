def myfunc(sentence, searched, pos_searched):
    out = 0
    if pos_searched == len(searched):
        return 1
    elif len(sentence) == 0:
        return 0

    pos = 0
    while pos < len(sentence):
        if sentence[pos] == searched[pos_searched]:
            out += myfunc(sentence[pos + 1:], searched, pos_searched + 1)
        pos += 1
    return out


cases = int(input())

for x in range(cases):
    temp = input()

    out = myfunc(temp, "welcome to code jam", 0)

    out = str(out)
    out = "0000" + out
    out = out[-4:]

    print("Case #{}: {}".format(x+1, out ))
