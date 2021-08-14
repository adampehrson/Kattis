words = input()

x = int(len(words) / 3)
out = ''

for i in range(x):
    if words[i] == words[i + x]:
        out = out + words[i]
    elif words[i] == words[i + 2*x]:
        out = out + words[i]
    else:
        out = out + words[i + x]
print(out)