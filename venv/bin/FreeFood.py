events = int(input())
days = set()


for i in range(events):
    event = list(map(int, input().split()))
    e = event[0]
    while e <= event[1]:
        days.add(e)
        e += 1
    i += 1

print(len(days))