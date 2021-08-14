import time

class Equation:
    def __init__(self, eq, data):
        self.eq = eq
        self.sign = data
        self.matr = Equation.matrix(self, eq)


    def matrix(self, eq):
        representation = [0,0,0]

        i = 0
        while eq[i] != "=":
            if eq[i] == "+":
                pass
            elif eq[i] == "-":
                self.sign = self.sign*-1
            else:
                temp = Equation.term(self,eq[i])
                if temp[0] == "-":
                    representation[temp[1]] -= temp[2]*self.sign
                    sign = 1
                if temp[0] == "+":
                    representation[temp[1]] += temp[2]*self.sign
                    sign = 1
            i += 1
        i += 1
        while i < len(eq):
            if eq[i] == "+":
                pass
            elif eq[i] == "-":
                self.sign = self.sign*-1
            else:
                temp = Equation.term(self,eq[i])
                if temp[0] == "-":
                    representation[temp[1]] += temp[2]*self.sign
                    sign = 1
                if temp[0] == "+":
                    representation[temp[1]] -= temp[2]*self.sign
                    sign = 1
            i += 1
        return representation

    def term(self, word):
        out = []
        if word[0] == "-":
            out.append("-")
            word = word[1:]
        else:
            out.append("+")
        if word[-1] == "x":
            out.append(0)
            word = word[:-1]
        elif word[-1] == "y":
            out.append(1)
            word = word[:-1]
        else:
            out.append(2)
        if len(word) != 0:
            out.append(int(word))
        else:
            out.append(1)
        return out




def gauss_elimination(matrix):
    if matrix[0][0] != 0:
        change = matrix[1][0] / matrix[0][0]
    else:
        change = 0
    for x in range(len(matrix[1])):
        matrix[1][x] = matrix[1][x] - matrix[0][x]*change

    if matrix[1][0] == 0 and matrix[1][1] != 0:
        change = matrix[0][1] / matrix[1][1]
    else:
        change = 0
    for x in range(len(matrix[1])):
        matrix[0][x] = matrix[0][x] - matrix[1][x] * change
    return matrix


def answer(matrix):
    out = []
    for x in range(2):
        if matrix[x][0] != 0 and matrix[x][1] == 0:
            temp = least_rational(-matrix[x][2], matrix[x][0])
            if len(temp) == 1:
                out.append("x"  + str(temp[0]))
            else:
                out.append("x"  + str(temp[0]) + "/" + str(temp[1]))
        elif matrix[x][1] != 0 and matrix[x][0] == 0:
            temp = least_rational(-matrix[x][2], matrix[x][1])
            if len(temp) == 1:
                out.append("y"  + str(temp[0]))
            else:
                out.append("y"  + str(temp[0]) + "/" + str(temp[1]))
    return out


def least_rational(a,b):
    if b < 0:
        a = a*-1
        b = b*-1
    i = 1
    a = int(a)
    b = int(b)

    while i*i <= a*a and i*i <= b*b:
        if a == int(a/i)*i and b == int(b/i)*i:
            a = int(a/i)
            b = int(b/i)
            i = 1
        i += 1


    if b == 1:
        return [a]
    else:
        return [a,b]


cases = int(input())

e = 0
while e < cases:

    eq1 = Equation(list(map(str, input().split())),  1)
    eq2 = Equation(list(map(str, input().split())), 1)

    linearsystem = gauss_elimination([eq1.matr, eq2.matr])
    final = answer(linearsystem)
    broken = False

    for x in range(2):
        if linearsystem[x][0] == 0 and linearsystem[x][1] == 0 and linearsystem[x][2] != 0:
            broken = True


    try:
        for x in range(2):
            if len(final) == 0 or broken == True:
                print("don't know")
                print("don't know")
                break
            if x == 0:
                if final[0][0] == "x":
                    print(final[0][1:])
                elif len(final) == 2 and final[1][0] == "x":
                    print(final[1][1:])
                else:
                    print("don't know")
            if x == 1:
                if final[0][0] == "y":
                    print(final[0][1:])
                elif len(final) == 2 and final[1][0] == "y" :
                    print(final[1][1:])
                else:
                    print("don't know")
    except:
        time.sleep(1)

    e += 1
    if e != cases:
        print()
        input()


