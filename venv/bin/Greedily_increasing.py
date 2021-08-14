import sys

amount = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

out = []
current = 0
numbers_inout = 0
for x in numbers:
    if x > current:
        current = x
        numbers_inout += 1
        out.append(x)


print(numbers_inout)
print(" ".join([str(x) for x in out]))
