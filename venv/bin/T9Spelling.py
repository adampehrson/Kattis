def t9(a):
    out = ''
    if a == 'a':
        out = '2'
    if a == 'b':
        out = '22'
    if a == 'c':
        out = '222'
    if a == 'd':
        out = '3'
    if a == 'e':
        out = '33'
    if a == 'f':
        out = '333'
    if a == 'g':
        out = '4'
    if a == 'h':
        out = '44'
    if a == 'i':
        out = '444'
    if a == 'j':
        out = '5'
    if a == 'k':
        out = '55'
    if a == 'l':
        out = '555'
    if a == 'm':
        out = '6'
    if a == 'n':
        out = '66'
    if a == 'o':
        out = '666'
    if a == 'p':
        out = '7'
    if a == 'q':
        out = '77'
    if a == 'r':
        out = '777'
    if a == 's':
        out = '7777'
    if a == 't':
        out = '8'
    if a == 'u':
        out = '88'
    if a == 'v':
        out = '888'
    if a == 'w':
        out = '9'
    if a == 'x':
        out = '99'
    if a == 'y':
        out = '999'
    if a == 'z':
        out = '9999'
    if a == ' ':
        out = '0'
    return out


a = int(input())
for x in range(a):
    sentence = input()
    numbers = []
    for w in sentence:
        numbers.append(t9(w))
    out = 'Case #' + str(x+1) + ': '
    for y in numbers:
        if out[-1] == y[0]:
            out = out + ' ' + y
        else:
            out = out + y
    print(out)