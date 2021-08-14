base = int(input())
pieces = int(input())

size = 0

for x in range(pieces):
    temp = list(map(int, input().split()))
    size = size + temp[0]*temp[1]

print(int(size / base))
