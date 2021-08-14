import sys

myrange = [0, 11]
while True:
    numb = int(input())
    if numb == 0:
        break
    info = input()
    if info == "right on":
        if numb in [x for x in range(myrange[0] + 1, myrange[1])]:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        myrange = [0,11]
    elif info == "too low" and numb > myrange[0]:
        myrange[0] = numb
    elif info == "too high" and numb < myrange[1]:
        myrange[1] = numb

