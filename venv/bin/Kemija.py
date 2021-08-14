
vowels = ['a', 'e', 'i', 'o', 'u']
sentence = input()
out = ''

i=0
while i < len(sentence):
    if sentence[i] in vowels:
        out = out + sentence[i]
        i += 3
    else:
        out = out + sentence[i]
        i += 1
print(out)