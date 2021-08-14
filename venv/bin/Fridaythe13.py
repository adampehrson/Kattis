tests = int(input())

for x in range(tests):
    kalendar = list(map(int, input().split()))
    months = list(map(int, input().split()))
    pos = 0
    fridays = 0
    for y in months:
        i = 1
        while i <= y:
            if i == 13 and pos % 7 == 5:
                fridays += 1
            i += 1
            pos += 1
    print(fridays)