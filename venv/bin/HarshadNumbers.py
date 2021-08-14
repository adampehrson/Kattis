n = input()

while True:
    i = 0
    tot = 0
    while i < len(n):
        tot = tot + int(n[i])
        i += 1
    if int(n) % tot == 0:
        print(n)
        break
    n = str(int(n) + 1)
