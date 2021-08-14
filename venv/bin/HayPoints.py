import time
cases = list(map(int, input().split()))
words = []

i = 0
while i < cases[0]:
    words.append(input().split())
    i += 1

words.sort()


i = 0
while i < cases[1]:
    out = 0
    description = []

    while True:
        a = input()
        if a == '.':
            break
        a = a.split()
        description = description + a

    description.sort()

    e = 0
    pos = 0
    while e < len(description) and pos < len(words):
        if description[e] < words[pos][0]:
            e += 1
        elif description[e] == words[pos][0]:
            out = out + int(words[pos][1])
            e += 1
        elif description[e] > words[pos][0]:
            pos += 1

    print(out)

    i += 1

