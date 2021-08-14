data = list(map(int, input().split()))

tasks = list(map(int, input().split()))
tasks.sort()
quiet = list(map(int, input().split()))
quiet.sort()

i = 0
tasks_pos = 0
quiet_pos = 0
for x in range(data[1]):
    while quiet_pos < len(quiet) and tasks[tasks_pos] > quiet[quiet_pos]:
        quiet_pos += 1
    if quiet_pos < len(quiet) and tasks[tasks_pos] <= quiet[quiet_pos]:
        i += 1
        tasks_pos += 1
        quiet_pos += 1
print(i)
