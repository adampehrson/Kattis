from sys import stdin

mydict = dict()

candidates = int(input())

for x in range(candidates):
    person = [stdin.readline().strip(), stdin.readline().strip()]
    mydict.update({person[0]: [person[1], 0]})


votes = int(input())

for x in range(votes):
    temp = input()
    if temp in mydict.keys():
        mydict[temp][1] += 1


largest = ["", 0]
draw = False
for x in mydict.keys():
    if mydict[x][1] > largest[1]:
        largest = mydict[x]
        draw = False
    elif mydict[x][1] == largest[1]:
        draw = True

if draw:
    print("tie")
else:
    print(largest[0])
