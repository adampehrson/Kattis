
current_time = list(map(int, input().split(":")))

wanted_time = list(map(int, input().split(":")))

diff = [0,0,0]

carryover = 0
for x in reversed(range(3)):
    if carryover == 1:
        diff[x] += 1
    if current_time > wanted_time:
        carryover = 1
        diff[x] += 60 - (current_time[x] - wanted_time[x])
    else:
        diff[x] += wanted_time[x] - current_time[x]
print(diff)


