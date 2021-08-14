word = input()
out = ''

i = 0
while i + 1 < len(word):
    if word[i] != word[i+1]:
        out = out + word[i]
    i += 1
out = out + word[-1]
print(out)