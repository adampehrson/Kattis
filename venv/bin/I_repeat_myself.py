cases = int(input())

for x in range(cases):
    sentence = input()

    for y in range(1, len(sentence)+1):
        temp = sentence[:y]
        newtemp = temp
        while len(temp) < len(sentence):
            temp += temp

        if sentence in temp:
            print(len(newtemp))
            break
