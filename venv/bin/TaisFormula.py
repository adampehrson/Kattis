tests = int(input())
lst = []

for i in range(tests):
    a = list(map(float, input().split()))
    lst.append(a)

i = 0
out = 0
while i + 1 < tests:
    out = out + ((lst[i][1] + lst[i+1][1]) / 2 ) * (lst[i+1][0] - lst[i][0])
    i += 1
print(out / 1000)