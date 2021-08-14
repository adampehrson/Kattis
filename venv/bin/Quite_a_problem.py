import sys

while True:

    line = sys.stdin.readline()
    if line == "":
        break

    line = line.lower()
    if "problem" in line:
        print("yes")
    else:
        print("no")