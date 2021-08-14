data = int(input())
out = [-1,-1]
for x in range(data):
    temp = list(map(int, input().split()))
    mark = 0
    if out == [-1,-1]:
        out = temp
    if temp[0] > out[1] or temp[1] < out[0]:
        print('edward is right')
        break
    if temp[0] > out[0]:
        out[0] = temp[0]
    if temp[1] < out[1]:
        out[1] = temp[1]
    if x == data-1:
        print('gunilla has a point')

