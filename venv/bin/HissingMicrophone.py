data = input()
out = 'no hiss'
i = 0
while i < len(data) - 1:
    if data[i] == 's' and data[i+1] == 's':
        out = 'hiss'
    i += 1
print(out)