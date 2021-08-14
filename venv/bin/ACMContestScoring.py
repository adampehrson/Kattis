log = []
solved = []
time = 0

while True:
    a = input().split()
    if len(a) == 1:
        break
    log.append(a)

logrev = list(reversed(log))

i = 0
while i < len(log):
    if logrev[i][2] == 'right':
        solved.append(logrev[i][1])
        time = time + int(logrev[i][0])
    elif logrev[i][2] == 'wrong':
        if solved.count(logrev[i][1]) != 0:
            time = time + 20
    i += 1
print(str(len(solved)) + ' ' + str(time))

