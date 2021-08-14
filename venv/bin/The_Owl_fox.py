import sys

cases = int(input())

for i in range(cases):
    numb = sys.stdin.readline().rstrip()
    removed = 0
    while numb[-1] == '0':
        removed += 1
        numb = numb[:-1]

    numb = str(int(numb) - 1)

    while removed != 0:
        numb += '0'
        removed -= 1
    print(int(numb))


