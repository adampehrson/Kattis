import sys



if __name__ == '__main__':
    wordtomath = dict()
    while True:
        current_line = sys.stdin.readline().strip()
        if current_line == "":
            break
        if current_line == "clear":
            wordtomath = dict()

        current_line = current_line.split()
        if current_line[0] == "def":
            wordtomath.update({current_line[1]: int(current_line[2])})

        if current_line[0] == "calc":
            finalout = ""
            for y in current_line[1:]:
                finalout += y + " "
            broken = False
            for x in current_line[1:][0::2]:
                if x not in wordtomath:
                    broken = True
                    break
            if not broken:
                out = wordtomath[current_line[1]]
                i = 2
                for x in current_line[3:][0::2]:
                    if current_line[i] == "+":
                        out += wordtomath[x]
                    elif current_line[i] == "-":
                        out -= wordtomath[x]
                    i += 2

                if out in wordtomath.values():
                    for y in wordtomath:
                        if wordtomath[y] == out:
                            finalout += y
                    print(finalout)
                else:
                    broken = True
            if broken:
                print("{} unknown".format(finalout))
