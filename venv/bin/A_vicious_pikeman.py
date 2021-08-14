first_line = list(map(int, input().split()))

data = list(map(int, input().split()))

problems = [data[3]]
repeating_seq = []
for x in range(1, first_line[0]):
    problems.append(((data[0]*problems[-1] + data[1]) % data[2]) + 1)
    if problems.count(problems[-1]) > 1:
        repeating_seq = problems[problems.index(problems[-1]):-1]


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