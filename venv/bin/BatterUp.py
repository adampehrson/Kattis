amount = int(input())
bases = 0

lst = list(map(int, input().split()))

for x in lst:
    if x == -1:
        amount = amount -1
    else:
        bases = bases + x

print(bases/amount)