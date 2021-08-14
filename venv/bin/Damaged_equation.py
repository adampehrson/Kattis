import operator



equation = list(map(int, input().split()))

mylist = [operator.mul, operator.add, operator.sub, operator.floordiv]

out = []
for x in range(4):
    for y in range(4):
        try:
            if mylist[x](equation[0], equation[1]) == mylist[y](equation[2], equation[3]):
                temp = [equation[0], x, equation[1], "=", equation[2], y, equation[3]]
                for z in [1, 5]:
                    if temp[z] == 0:
                        temp[z] = "*"
                    if temp[z] == 1:
                        temp[z] = "+"
                    if temp[z] == 2:
                        temp[z] = "-"
                    if temp[z] == 3:
                        temp[z] = "/"
                out.append(temp)
        except ZeroDivisionError:
            pass



if len(out) == 0:
    print("problems ahead")
else:
    for x in out:
        myprint = ""
        for y in x:
            myprint += str(y) + " "
        print(myprint[:-1])