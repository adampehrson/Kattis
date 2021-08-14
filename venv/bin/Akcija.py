no_items = int(input())

items = []

for x in range(no_items):
    items.append(int(input()))

items.sort()

items.sort()
items.reverse()

price = 0
n = 0
while n < len(items):
    if n % 3 != 2:
        price += items[n]
    n += 1

print(price)
