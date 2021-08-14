def operator(x):
    if x == 0:
        return '+'
    if x == 1:
        return '-'
    if x == 2:
        return '*'
    if x == 3:
        return '/'


def arithmetic(target):



    a = 0
    while a < 4:
        op = ''
        op = op + operator(a)
        b = 0
        while b < 4:
            temp1 = op + operator(b)
            c = 0
            while c < 4:
                temp = temp1 + operator(c)
                out = [4,temp[0],4,temp[1],4,temp[2],4]
                placeholder = [4,temp[0],4,temp[1],4,temp[2],4]
                i = 1

                while i < len(out):
                    if out[i] == '*':
                        out[i-1] = out[i-1] * out[i+1]

                        out.pop(i)
                        out.pop(i)

                    elif out[i] == '/':
                        out[i-1] = out[i-1] // out[i+1]
                        out.pop(i)
                        out.pop(i)
                    else:
                        i += 2
                i = 1
                while i < len(out):
                    if out[i] == '+':
                        out[i-1] = out[i-1] + out[i+1]
                        out.pop(i)
                        out.pop(i)
                    elif out[i] == '-':
                        out[i-1] = out[i-1] - out[i+1]
                        out.pop(i)
                        out.pop(i)
                    else:
                        i += 2

                if out[0] == target:
                    equation = ''
                    for x in placeholder:
                        equation += str(x) + ' '
                    equation += '= ' + str(out[0])
                    return equation


                c += 1
            b += 1

        a += 1
    return 'no solution'

cases = int(input())

for i in range(cases):
    print(arithmetic(int(input())))
