import math

data = list(map(int, input().split(' ')))
i = 0
sqrrooted = math.sqrt(data[1]*data[1] + data[2]*data[2])
while i < data[0]:
    a = int(input())
    if a <= sqrrooted:
        print('DA')
    else:
        print('NE')
    i +=1