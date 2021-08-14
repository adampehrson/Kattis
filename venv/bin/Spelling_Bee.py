import sys

letters = input()

out = []
dictionary_length = int(input())

for x in range(dictionary_length):
    temp = sys.stdin.readline().strip()
    broken = False


    if letters[0] in temp:
        for y in temp:
            if y not in letters:
                broken = True
                break
        if not broken and len(temp) >= 4:
            out.append(temp)

for x in out:
    print(x)







