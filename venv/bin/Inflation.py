balloons = int(input())
lst = []
i = 1
while i <= balloons:
    lst.append(i)
    i += 1

tanks = list(map(int, input().split()))
tanks = sorted(tanks)

largest = 2
i = 0
while i < len(lst):
    if i + 1 < tanks[i]:
        largest = 2
        break
    if largest > tanks[i] / (i + 1) :
        largest = tanks[i] / (i + 1)
    i += 1
if largest > 1:
    print('IMPOSSIBLE')
else:
    print(largest)