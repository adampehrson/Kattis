input()

n = input().split()
tot = 0

for x in n:
    if x[0] == '-':
        tot = tot + int(x[1:])

print(tot)

