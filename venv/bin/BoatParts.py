tests = list(map(int, input().split()))
parts = []
pos = 0

for i in range(tests[1]):
    a = input()
    if a not in parts:
        pos = i
        parts.append(a)

pos += 1
if len(parts) == tests[0]:
    print(pos)
else:
    print('paradox avoided')