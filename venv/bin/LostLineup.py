people = int(input())
line = list(map(int, input().split()))
out = ''
for i in range(people):
    if i == 0:
        out = out + '1 '
    else:
        out = out + str(line.index(i-1) + 2) + ' '
print(out[:-1])