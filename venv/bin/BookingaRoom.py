rooms = list(map(int, input().split()))
occupied = [0]
for x in range(rooms[1]):
    occupied.append(int(input()))
occupied.sort()
i = 0
while i <= rooms[0]:
    if i >= len(occupied):
        print(i)
        break
    if occupied[i] != i:
        print(i)
        break
    i += 1

if i == rooms[0] + 1:
    print('too late')