import fileinput
for line in fileinput.input():
    line = "x = " + line
    exec(line)
    print("{0:.2f}".format(x))