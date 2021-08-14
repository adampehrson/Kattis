cases = int(input())

for x in range(cases):
    data = input().split()
    firstdict = dict()
    seconddict = dict()
    baseto = len(data[2])
    basefrom = len(data[1])
    input_number = data[0]

    i = 0
    while i < len(data[1]):
        temp = {data[1][i]: i}
        firstdict.update(temp)
        i += 1

    i = 0
    while i < len(data[2]):
        temp = {i: data[2][i]}
        seconddict.update(temp)
        i += 1

    mynumber_base10 = 0
    i = len(input_number) - 1
    for y in input_number:
        mynumber_base10 += firstdict[y]*(len(firstdict)**i)
        i -= 1


    i = 0
    while mynumber_base10 // (len(seconddict))**i != 0:
        i += 1
    i -= 1

    mynumber_alienbase = ""
    while i >= 0:
        temp = mynumber_base10 // (len(seconddict))**i
        mynumber_base10 = mynumber_base10 - temp*(len(seconddict))**i
        mynumber_alienbase = mynumber_alienbase + seconddict[temp]
        i -= 1

    print("Case #{}: {}".format(x+1, mynumber_alienbase))