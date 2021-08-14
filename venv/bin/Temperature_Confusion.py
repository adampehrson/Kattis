start_temp = list(map(int, input().split("/")))

divisor = start_temp[1] * 9

numerator = start_temp[0] - 32*start_temp[1]
numerator = numerator * 5


while True:
    i = 2
    while i <= divisor or i <= numerator:
        if divisor % i == 0 and numerator % i == 0:
            divisor = divisor / i
            numerator = numerator / i
            break
        i += 1

    if i > divisor and i > numerator:
        break

print(str(int(numerator)) + "/" + str(int(divisor)))
