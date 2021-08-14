data = list(map(int, input().split()))

items = list(map(int, input().split()))

items.sort()

i = 1
while i < len(items):
    if items[i] + items[i-1] > data[1]:
        break
    i += 1

print(i)