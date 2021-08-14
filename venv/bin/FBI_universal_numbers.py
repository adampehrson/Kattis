mydict = dict()
mystr = "ACDEFHJKLMNPRTVWX"
for x in range(10):
    mydict.update({str(x): x})


i = 9
for x in range(65,91):
    temp = chr(x)
    if temp in mystr:
        i += 1
    mydict.update({chr(x): i})

mydict["B"] = 8
mydict["G"] = mydict["C"]
mydict["I"] = 1
mydict["O"] = 0
mydict["Q"] = 0
mydict["S"] = 5
mydict["U"] = mydict["V"]
mydict["Y"] = mydict["V"]
mydict["Z"] = 2


cases = int(input())

for x in range(cases):
    number = input().split()[1]
    out = 0
    check_digit = 0
    mylist = [2, 4, 5, 7, 8, 10, 11, 13]

    for y in range(8):
        check_digit += mylist[y]*mydict[number[y]]
        out += mydict[number[y]]*(27**(8 - y - 1))

    if check_digit % 27 == mydict[number[-1]]:
        print("{} {}".format(x+1, out))
    else:
        print("{} {}".format(x+1, "Invalid"))


