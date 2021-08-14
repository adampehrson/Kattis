first_line = list(map(int, input().split()))

data = list(map(int, input().split()))

previous = data[3]
problems = [previous]
for x in range(1, first_line[0]):
    current = ((data[0]*previous + data[1]) % data[2]) + 1
    problems.append(current)
    previous = current

problems.sort()

time = 0
penalty = 0
amount = 0
for x in problems:
    time += x
    if time <= first_line[1]:
        penalty += time
        amount += 1
    else:
        break
print("{} {}".format(amount, penalty % 1000000007))