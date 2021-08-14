import sys

mydict = dict()

while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    line = line.split()

    mydict.update({line[1]: line[0]})

while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break

    if line in mydict:
        print(mydict[line])
    else:
        print("eh")
