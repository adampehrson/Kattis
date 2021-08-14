days = int(input())
temps = list(map(int, input().split()))
out = [0,0]
i = 0
while i < days - 2:
    if temps[i] > temps[i+2]:
        temp = temps[i]
    else:
        temp = temps[i+2]
    if i == 0:
        out[0] = i + 1
        out[1] = temp
    elif temp < out[1]:
        out[0] = i + 1
        out[1] = temp
    i += 1
print(str(out[0]) + ' ' + str(out[1]))