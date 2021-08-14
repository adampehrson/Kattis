lst = list(map(int, input().split()))

i = 0
denied = 0
current = 0
while i < lst[1]:
    event = input().split()
    if event[0] == 'enter':
        if current + int(event[1]) <= lst[0]:
            current = current + int(event[1])
        else:
            denied += 1
    if event[0] == 'leave':
        current = current - int(event[1])
    i += 1
print(denied)