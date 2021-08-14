tests = int(input())


for i in range(tests):
    case = input().split()
    number = list(map(int, case[1].split('/')))

    e = 0
    out = 0
    while number[0] != number[1]:
        if number[0] > number[1]:
            number[0] = number[0] - number[1]
            out = out + 2**(e+1)
        elif number[1] > number[0]:
            number[1] = number[1] - number[0]
            out = out + 2**e
        e += 1
    out += 1
    out = str(case[0]) + ' ' + str(out)
    print(out)
