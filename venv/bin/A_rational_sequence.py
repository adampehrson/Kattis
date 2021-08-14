cases = int(input())

for x in range(cases):
    case = input().split()
    number = list(map(int, case[1].split('/')))

    up = 0
    to_right = False
    if number[1] == 1:
        number[1] = number[0] + 1
        number[0] = 1
    else:
        while not to_right:
            if number[0] > number[1]:
                up += number[0] // number[1]
                number[0] = number[0] % number[1]
            else:
                up += 1
                number[1] = number[1] - number[0]
                to_right = True
        number[0] = number[0] + number[1]
        up -= 1
        number[1] = number[1] + number[0]*up

    print("{} {}/{}".format(x+1, number[0], number[1]))
