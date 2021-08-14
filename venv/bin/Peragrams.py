sentence = input()

mydict = dict()

for x in sentence:
    if x in mydict:
        temp = mydict.get(x) + 1
        if temp % 2 == 0:
            temp = 0
        else:
            temp = 1
        temp = {x: temp}
        mydict.update(temp)
    else:
        mydict.update({x: 1})

out = 0
single = False

for x in mydict.values():
    if x == 1:
        if single:
            out += 1
        else:
            single = True

print(out)
