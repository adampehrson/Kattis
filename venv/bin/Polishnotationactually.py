import sys
i = 0


def dooperation(a,b,c):
    if a == '+':
        return int(b) + int(c)
    if a == '-':
        return int(b) - int(c)
    if a == '*':
        return int(b) * int(c)

def checkoperand(a):
    if a == '-' or a == '*' or a == '+':
        return True
    return False


def checkint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


i = 1
for line in sys.stdin:
    formula = line.split()
    e = len(formula) - 3
    while e >= 0:
        if checkoperand(formula[e]):
            if checkint(formula[e+1]) and checkint(formula[e+2]):
                temp = dooperation(formula[e], formula[e+1], formula[e+2])
                formula.pop(e)
                formula.pop(e)
                formula.pop(e)
                formula.insert(e,temp)
        e -= 1

    out = 'Case ' + str(i) + ':'
    for x in formula:
        out = out + ' ' + str(x)
    print(out)
    i += 1






