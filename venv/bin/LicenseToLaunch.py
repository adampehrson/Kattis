days = int(input())
junk = list(map(int, input().split()))
empty = []

for i in range(days):
    empty.append(junk[i])


a = sorted(empty)
print(empty.index(a[0]))