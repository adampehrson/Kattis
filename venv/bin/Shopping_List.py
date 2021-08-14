data = list(map(int, input().split()))

items = input().split()

i = 1
while i < data[0]:
    temp = input().split()
    tempitems = []
    for x in temp:
        if x in items:
            tempitems.append(x)
    items = tempitems
    i += 1

print(len(items))

items.sort()
for x in items:
    print(x)