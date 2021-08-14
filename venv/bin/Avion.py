tot = []
out = ''
i = 0
while i < 5:
    blimp = input()
    if blimp.find('FBI') != -1:
        out = out + str(i+1) + ' '
    i += 1

if out == '':
    print('HE GOT AWAY!')
else:
    print(out[:-1])