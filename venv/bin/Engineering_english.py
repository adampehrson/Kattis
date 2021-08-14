import sys


words = []


while True:
    temp = sys.stdin.readline().strip()
    current_line = []
    if temp == "":
        break
    temp = temp.split()
    for x in temp:

        if x.lower() in words:
            current_line.append(".")
        else:
            words.append(x.lower())
            current_line.append(x)
    out = ""

    for x in current_line:
        out = out + x + " "

    print(out)

