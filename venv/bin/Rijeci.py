a = int(input())

out = [1, 0]

i = 0
while i < a:
    temp = out[0] + out[1]
    out[0] = out[1]
    out[1] = temp


    i += 1

print(str(out[0]) + ' ' + str(out[1]))