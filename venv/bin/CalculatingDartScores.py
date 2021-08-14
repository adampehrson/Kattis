score = input()
gotten = False


a = 1
b = 1
c = 1

while a <= 20:
    if a + b + c == score:
        gotten = True
        break
    a += 1




if gotten == False:
    while b <= 60:
        if a + b + c == score:
            out = True
            break
        b += 1

if gotten == False:
    while c <= 60:
        if a + b + c == score:
            out = True
            break
        c += 1

