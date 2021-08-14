tests = int(input())

for x in range(tests):
    grades = list(map(int, input().split()))
    i = 1
    temp = 0
    while i < len(grades):
        temp = temp + grades[i]
        i += 1
    average = temp / grades[0]

    above = 0
    i = 1
    while i < len(grades):
        if grades[i] > average:
            above += 1
        i += 1
    out = (100*above / grades[0]) + 0.0005
    print(str(out)[:str(out).index('.')+4] + '%')