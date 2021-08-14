def encode(a):
    out = ""
    i = 0
    while i < len(a):
        temp = 1
        while i + 1 < len(a) and a[i] == a[i+1]:
            temp += 1
            i += 1
        out = out + a[i] + str(temp)
        i += 1
    return out

def decode(a):
    out = ""
    i = 0
    while i < len(a):
        temp = a[i]*int(a[i+1])
        out = out + temp
        i += 2
    return out



a = input()
if a[0] == 'E':
    print(encode(a[2:]))

else:
    print(decode(a[2:]))