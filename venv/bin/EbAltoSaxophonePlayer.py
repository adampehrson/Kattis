#Creating array:


def checkpressed(fingers, presses, index):
    if not fingers[index]:
        fingers[index] = True
        presses[index] += 1



def press(fingers, presses, note):
    if note == 'c':
        for x in [2, 3, 4, 7, 8, 9, 10]:
            checkpressed(fingers, presses, x)
        for a in [1, 5, 6]:
            fingers[a] = False
    if note == 'd':
        for x in [2, 3, 4, 7, 8, 9]:
            checkpressed(fingers, presses, x)
        for a in [1, 5, 6, 10]:
            fingers[a] = False
    if note == 'e':
        for x in [2, 3, 4, 7, 8]:
            checkpressed(fingers, presses, x)
        for a in [1, 5, 6, 9, 10]:
            fingers[a] = False
    if note == 'f':
        for x in [2, 3, 4, 7]:
            checkpressed(fingers, presses, x)
        for a in [1, 5, 6, 8, 9, 10]:
            fingers[a] = False
    if note == 'g':
        for x in [2, 3, 4]:
            checkpressed(fingers, presses, x)
        for a in [1, 5, 6, 7, 8, 9, 10]:
            fingers[a] = False
    if note == 'a':
        for x in [2, 3]:
            checkpressed(fingers, presses, x)
        for a in [1, 4, 5, 6, 7, 8, 9, 10]:
            fingers[a] = False
    if note == 'b':
        for x in [2]:
            checkpressed(fingers, presses, x)
        for a in [1, 3, 4, 5, 6, 7, 8, 9, 10]:
            fingers[a] = False
    if note == 'C':
        for x in [3]:
            checkpressed(fingers, presses, x)
        for a in [1, 2, 4, 5, 6, 7, 8, 9, 10]:
            fingers[a] = False
    if note == 'D':
        for x in [1, 2, 3, 4, 7, 8, 9]:
            checkpressed(fingers, presses, x)
        for a in [5, 6, 10]:
            fingers[a] = False
    if note == 'E':
        for x in [1, 2, 3, 4, 7, 8]:
            checkpressed(fingers, presses, x)
        for a in [5, 6, 9, 10]:
            fingers[a] = False
    if note == 'F':
        for x in [1, 2, 3, 4, 7]:
            checkpressed(fingers, presses, x)
        for a in [5, 6, 8, 9, 10]:
            fingers[a] = False
    if note == 'G':
        for x in [1, 2, 3, 4]:
            checkpressed(fingers, presses, x)
        for a in [5, 6, 7, 8, 9, 10]:
            fingers[a] = False
    if note == 'A':
        for x in [1, 2, 3]:
            checkpressed(fingers, presses, x)
        for a in [4, 5, 6, 7, 8, 9, 10]:
            fingers[a] = False
    if note == 'B':
        for x in [1, 2]:
            checkpressed(fingers, presses, x)
        for a in [3, 4, 5, 6, 7, 8, 9, 10]:
            fingers[a] = False






tests = int(input())

for x in range(tests):
    fingers = [False] * 11
    presses = [0] * 11
    song = input()

    i = 0
    while i < len(song):
        press(fingers, presses, song[i])
        i += 1

    out = ''
    i = 1
    while i <= 10:
        out = out + str(presses[i]) + ' '
        i += 1

    out = out[:-1]
    print(out)















