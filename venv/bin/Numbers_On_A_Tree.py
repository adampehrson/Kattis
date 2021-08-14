data = input().split()

i = 0
offset = 0
if len(data) == 2:
    while i < len(data[1]):
        if data[1][i] == "L":
            offset += 2**(len(data[1]) - i - 1)
        else:
            offset += 2 ** (len(data[1]) - i)
        i += 1

print(2**(int(data[0]) + 1) - 1 - offset)