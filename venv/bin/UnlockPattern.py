from math import sqrt
code = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
dist = 0
i = 1
while i < 10:
    e = 0
    while e < 3:
        if code[e].count(i) != 0:
            start = [e, code[e].index(i)]
        if code[e].count(i+1) != 0:
            end = [e, code[e].index(i+1)]
        e += 1
    temp = sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2)
    dist = dist + temp
    i += 1
print(dist)