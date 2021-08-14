import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True




cases = int(input())

for x in range(cases):
    data = list(map(int, input().split()))
    current = [data[0]]
    steps = 0

    while data[1] not in current:
        new_numbers = []
        for y in current:
            for z in range(4):
                for w in range(10):
                    temp = int(str(y)[:z] + str(w) + str(y)[z+1:])
                    if temp >= 1000 and is_prime(temp):
                        new_numbers.append(temp)
        current = set(new_numbers)
        steps += 1
        if not current:
            break
    if not current:
        print("Impossible")
    else:
        print(steps)




