data = list(map(int, input().split()))
points = list(map(int, input().split()))
out = 0

i = 0
pos = 0

while i < data[0]:
    out = out + (points[i] - pos) * (100 + i * data[1])
    pos = points[i]
    i += 1

out = out + (data[2] - pos) * (100 + i * data[1])
print(out/100)

