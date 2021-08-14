def coord(b):
    x = 0
    y = 0
    if int(b) % 2 == 1:
        x = 1
    if int(b) > 1:
        y = 1
    return str(x) + ' ' + str(y)



a = input()
out = [0,0]
i = 0
while i < len(a):
    c = coord(a[i]).split()
    out[0] = out[0] * 2 + int(c[0])
    out[1] = out[1] * 2 + int(c[1])
    i += 1

print(str(len(a)) + ' ' +  str(out[0]) + ' ' + str(out[1]))



