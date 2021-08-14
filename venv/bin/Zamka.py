least = input()
most = input()
total = int(input())
i = 0
while i >= 0:
    i = 0
    a = 0
    while i < len(least):
        a = a + int(least[i])
        i += 1
    if a == total:
        print(least)
        break
    least = str(int(least) + 1)

while i >= 0:
    i = 0
    a = 0
    while i < len(most):
        a = a + int(most[i])
        i += 1
    if a == total:
        print(most)
        break
    most = str(int(most) - 1)
