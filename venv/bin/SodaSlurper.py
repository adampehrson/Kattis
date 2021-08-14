b = list(map(int, input().split(' ')))
b[0] = b[1] + b[0]
i = 0
drinks = 0
while i == 0:
    if b[0] >= b[2]:
        drinks = drinks + 1
        b[0] = b[0] - b[2] + 1
    if b[0] < b[2]:
        break
print(drinks)





