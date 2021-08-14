import  sys




mydict = dict()

while True:
    line = sys.stdin.readline()
    if line == "":
        break

    line = line.split()

    if line[0] == "define":
        temp = {line[2]: int(line[1])}
        mydict.update(temp)




    if line[0] == "eval":
        if line[1] not in mydict or line[3] not in mydict:
            print("undefined")
        elif line[2] == "<":
            if mydict[line[1]] < mydict[line[3]]:
                print("true")
            else:
                print("false")
        elif line[2] == ">":
            if mydict[line[1]] > mydict[line[3]]:
                print("true")
            else:
                print("false")
        elif line[2] == "=":
            if mydict[line[1]] == mydict[line[3]]:
                print("true")
            else:
                print("false")
        else:
            print("false")

