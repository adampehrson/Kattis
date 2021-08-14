def rotate(a):
    amount = 0
    for x in a:
        amount = amount + ord(x) - 65

    out = []
    i = 0
    while i < len(a):
        temp = ord(a[i]) - 65
        temp = (temp + amount) % 26
        out.append(temp)
        i += 1
    return out


word = input()
first = word[:int(len(word)/2)]
last = word[int(len(word)/2):]


first = rotate(first)
last = rotate(last)

i = 0
while i < len(first):
    first[i] = (first[i] + last[i]) % 26
    i += 1

out = ''
for x in first:
    out = out + chr(x+65)

print(out)
