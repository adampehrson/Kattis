amount = int(input())

out = 1 - amount
for x in range(amount):
    out += int(input())

print(out)
