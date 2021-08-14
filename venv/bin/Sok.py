amount = list(map(int, input().split()))
needed = list(map(int, input().split()))
prop = []
i = 0
while i < 3:
    prop.append(amount[i] / needed[i])
    i += 1

prop.sort()
i = 0
while i < 3:
    amount[i] = amount[i] - (needed[i] * prop[0])
    i += 1

out = ''
for x in amount:
    out = out + str(x) + ' '

print(out[:-1])