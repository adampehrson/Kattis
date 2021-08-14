numbers = list(map(int, input().split()))

out = numbers[0]*numbers[1] // numbers[2]

temp = numbers[0]*numbers[1] % numbers[2]

print(str(out) + str(temp / numbers[2])[1:] )