number = int(input())
qaly = 0.0
i = 0
while i < number:
    lst = list(map(float, input().split()))
    qaly = qaly + lst[0]*lst[1]
    i += 1
print(qaly)
