x = int(input())
sum = 0
i = 0
while i < x:
    y = input()
    sum = sum + int(y[0:-1])**int(y[-1])
    i += 1

print(sum)