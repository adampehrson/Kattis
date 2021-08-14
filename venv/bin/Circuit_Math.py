def opand(a,b):
    if a == "T" and b == "T":
        return "T"
    return "F"

def opor(a,b):
    if a == "T" or b == "T":
        return "T"
    return "F"

def opnor(a):
    if a == "F":
        return "T"
    return "F"


variables = int(input())
values = input().split()
i = 0

test = {}

for x in range(variables):
    temp = chr(x + 65)
    tempkey = {temp: values[x]}
    test.update(tempkey)



equation = input().split()

i = 0
while i < len(equation):
    if equation[i] in test:
        equation[i] = test[equation[i]]
    i += 1


customboolean = ['T', 'F']

while len(equation) != 1:
    i = 1
    while i < len(equation):
        if equation[i] == "-":
            if equation[i-1] in customboolean:
                equation[i-1] = opnor(equation[i-1])
                equation.pop(i)

                break
            elif i == 1:
                i += 1
        if equation[i] == "+":
            if equation[i - 1] in customboolean and equation[i-2] in customboolean:
                equation[i -2] = opor(equation[i - 1], equation[i-2])
                equation.pop(i)
                equation.pop(i-1)

                break

        if equation[i] == "*":
            if equation[i - 1] in customboolean and equation[i - 2] in customboolean:
                equation[i - 2] = opand(equation[i - 1], equation[i-2])
                equation.pop(i)
                equation.pop(i-1)

                break
        i += 1


print(equation[0])
