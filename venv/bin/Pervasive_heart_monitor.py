import sys

while True:
    data = sys.stdin.readline().strip()
    if data == "":
        break
    data = data.split()


    out = 0
    amount = 0
    name = ""
    for x in range(len(data)):
        try:
            test = float(data[x])
            out += test
            amount += 1
        except ValueError:
            name += data[x] + " "

    print("{} {}".format(out/amount, name[:-1]))
