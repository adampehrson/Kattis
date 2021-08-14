words = int(input())

sentence_dutch = input().split()

mydict = dict()
myotherdict = dict()
mydict_length = int(input())

for x in range(mydict_length):
    temp = input().split()
    if temp[0] not in mydict:
        if temp[2] == "correct":
            mydict.update({temp[0]: [1,0]})
        else:
            mydict.update({temp[0]: [0,1]})
    elif temp[0] in mydict:
        if temp[2] == "correct":
            mydict[temp[0]] = [mydict[temp[0]][0] + 1, mydict[temp[0]][1]]
        else:
            mydict[temp[0]] = [mydict[temp[0]][0], mydict[temp[0]][1] + 1]
    myotherdict.update({temp[0]: temp[1]})



sentence = ""
correct = 1
total = 1

for x in sentence_dutch:
    correct = correct * mydict[x][0]
    total = total * (mydict[x][0] + mydict[x][1])
    sentence = sentence + myotherdict[x] + " "


if total == 1:
    print(sentence[:-1])
    if correct == 1:
        print("correct")
    else:
        print("incorrect")

else:
    print("{} correct".format(correct))
    print("{} incorrect".format(total - correct))
