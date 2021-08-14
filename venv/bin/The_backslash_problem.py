from sys import stdin

special_characters = []

for x in range(33, 43):
    special_characters.append(chr(x))

for x in range(91, 94):
    special_characters.append(chr(x))


while True:
    interpretation = stdin.readline()

    if interpretation == "":
        break

    interpretation = int(interpretation)

    sentence = input()

    i = 0
    while i < interpretation:
        temp = ""
        for x in sentence:
            if x in special_characters:
                temp += '\\' + x
            else:
                temp += x
        sentence = temp
        i += 1
    print(sentence)
