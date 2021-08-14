def window(a):
    current = 3
    a = (a - 2018)*12
    while current < a:
        current += 26

    if a + 12 > current:
        return 'yes'
    else:
        return 'no'


print(window(int(input())))



