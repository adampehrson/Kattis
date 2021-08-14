import sys

amount = int(input())

numbers = []

for x in range(amount):
    numbers.append(int(sys.stdin.readline()))

right = sum(numbers)

left = 0

out = 0

for x in range(len(numbers)):
    left += numbers[x]**2
    right -= numbers[x]
    if left * right > out:
        out = left*right

print(out)