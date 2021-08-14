numpad = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

amount = int(input())

words = []
for x in range(amount):
    words.append(input())


presses = input()

valid = 0

i = 0
while i < len(words):
    e = 0
    pos = 0
    broken = False
    while e < len(presses) and pos < len(words[i]):
        if words[i][pos] in numpad[int(presses[e])]:
            pos += 1
        else:
            broken = True
            break
        e += 1
    if not broken:
        valid += 1
    i += 1

print(valid)
