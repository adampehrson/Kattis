data = list(map(int, input().split()))

bricks = list(map(int, input().split()))

layer = 0
current_width = 0

out = "YES"
i = 0
while layer <= data[0] and current_width < data[1] and i < data[2]:
    current_width += bricks[i]
    if current_width == data[1]:
        current_width = 0
        layer += 1
    if current_width > data[1]:
        out = "NO"
    if layer > data[0] and current_width != 0:
        out = "NO"
    i += 1


print(out)