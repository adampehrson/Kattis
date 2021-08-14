word = input()
letters = input()

guessed = 0
wrong = 0

for x in letters:
    if word.count(x) != 0:
        guessed += word.count(x)
    if guessed == len(word):
        break
    if word.count(x) == 0:
        wrong += 1
    if wrong == 10:
        break

if wrong >= 10:
    print('LOSE')
if guessed == len(word):
    print('WIN')