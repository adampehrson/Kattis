tests = int(input())

out = 'yes'

words = []
rhymes = []

i = 0
while i < tests:
    lst = input().split()
    words.append(lst)
    i += 1


i = 0
while i < len(words):
    if len(words[i][0]) < 3 and words[i][0] == words[i][2] and words[i][1] == 'is':
        rhymes.append(words[i][0])
    i += 1


i = 0
while i < len(words):
    if words[i][1] == 'is':
        if words[i][0][-3:] != words[i][2][-3:]:
            out = 'wait what?'
            if words[i][0][-2:] == words[i][2][-2:]:
                if rhymes.count(words[i][0][-2:]) != 0:
                    out = 'yes'
            if words[i][0][-1:] == words[i][2][-1:]:
                if rhymes.count(words[i][0][-1:]) != 0:
                    out = 'yes'
            if out == 'wait what?':
                break

    if words[i][1] == 'not':
        if words[i][0][-3:] == words[i][2][-3:]:
            out = 'wait what?'
            break
        if words[i][0][-2:] == words[i][2][-2:] and rhymes.count(words[i][0][-2:]) != 0:
            out = 'wait what?'
            break
        if words[i][0][-1:] == words[i][2][-1:] and rhymes.count(words[i][0][-1:]) != 0:
            out = 'wait what?'
            break
    i += 1
print(out)
