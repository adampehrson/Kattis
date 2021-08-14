import time

i = 0
while i == 0:
    try:
        data = list(map(int, input().split()))
    except EOFError:
        break
    data.sort()
    print(data[1] - data[0])