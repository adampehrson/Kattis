code = input()

i = 0
pos = 0
for x in code:
    if x.isupper():
        while (pos + i) % 4 != 0:
            i += 1
    pos += 1
print(i)