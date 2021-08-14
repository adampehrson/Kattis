import math
n = int(input())
score = 0

while n % 2 == 0:
    score += 1
    n = n / 2

i = 3
while i <= int(math.sqrt(n)) + 1:

    while n % i == 0:
        score += 1
        n = n / i
    i = i + 2

if n > 1:
    score += 1

print(score)