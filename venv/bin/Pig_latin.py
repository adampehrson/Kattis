import sys

mylist = ["a", "e", "i", "o", "u", "y"]


while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break

    line = line.split()

    out = []

    for x in line:
        if x[0] in mylist:
            out.append(x + "yay")

        else:
            pos = 1
            while x[pos] not in mylist:
                pos += 1
            out.append(x[pos:] + x[:pos] + "ay")

    myout = ""
    for x in out:
        myout += x + " "

    print(myout[:-1])
