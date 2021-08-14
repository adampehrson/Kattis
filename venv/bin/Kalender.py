lst = list(map(int, input().split()))
offset = 0

if lst[1] == 1:
    offset = 4
if lst[1] == 2:
    offset = 0
if lst[1] == 3:
    offset = 0
if lst[1] == 4:
    offset = 3
if lst[1] == 5:
    offset = 5
if lst[1] == 6:
    offset = 1
if lst[1] == 7:
    offset = 3
if lst[1] == 8:
    offset = 6
if lst[1] == 9:
    offset = 2
if lst[1] == 10:
    offset = 4
if lst[1] == 11:
    offset = 0
if lst[1] == 12:
    offset = 2

offset = (offset + lst[0] -1) % 7

if offset == 1:
    print('Monday')
if offset == 2:
    print('Tuesday')
if offset == 3:
    print('Wednesday')
if offset == 4:
    print('Thursday')
if offset == 5:
    print('Friday')
if offset == 6:
    print('Saturday')
if offset == 0:
    print('Sunday')