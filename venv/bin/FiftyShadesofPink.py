tests = int(input())

out = 0

i = 0
while i < tests:
    word = input()
    word = word.lower()
    if word.count('pink') > 0:
        out += 1
    elif word.count('rose') > 0:
        out += 1
    i += 1

if out == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(out)