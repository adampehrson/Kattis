a = input()
b = input()
newa = ''
newb = ''

i = 1
while i <= len(a) and i <= len(b):
    if a[-i] > b[-i]:
        newa = a[-i] + newa
    elif a[-i] == b[-i]:
        newa = a[-i] + newa
        newb = b[-i] + newb
    else:
        newb = b[-i] + newb
    i += 1

i -= 1
newa = a[:-i] + newa
newb = b[:-i] + newb

if newa == '':
    print('YODA')
else:
    print(int(newa))

if newb == '':
    print('YODA')
else:
    print(int(newb))