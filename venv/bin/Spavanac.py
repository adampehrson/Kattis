time = list(map(int, input().split(' ')))

if time[1] < 45:
    time[0] = (time[0] - 1) % 24
    time[1] = (time[1] - 45) % 60
else:
    time[1] = time[1] - 45

print(str(time[0]) + ' ' + str(time[1]))
