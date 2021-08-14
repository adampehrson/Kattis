tests = int(input())

for x in range(tests):
    tempnumber_60 = input()
    number_60 = []

    i = 0
    while i < len(tempnumber_60):
        if tempnumber_60[i] == ",":
            if i == len(tempnumber_60) - 1 or tempnumber_60[i+1] == ",":
                number_60.append(0)
                i += 1
            else:
                i += 1
        else:
            currentpos = ""
            while i < len(tempnumber_60) and tempnumber_60[i] != ",":
                currentpos = currentpos + tempnumber_60[i]
                i += 1
            number_60.append(int(currentpos))

    number_10 = 0

    i = 0
    while i < len(number_60):
        number_10 = number_10 + number_60[i]*(60**(len(number_60)- i - 1))
        i += 1
    print(number_10)