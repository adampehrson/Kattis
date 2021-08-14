cases = int(input())

i = 0
while i < cases:
    numbers = list(map(int, input().split()))
    if numbers[0] + numbers[1] == numbers[2]:
        print('Possible')
    elif numbers[0] - numbers[1] == numbers[2] or numbers[1] - numbers[0] == numbers[2]:
        print('Possible')
    elif numbers[1] / numbers[0] == numbers[2] or numbers[0] / numbers[1] == numbers[2]:
        print('Possible')
    elif numbers[0] * numbers[1] == numbers[2]:
        print('Possible')
    else:
        print('Impossible')
    i += 1
