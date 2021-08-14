questions = int(input())

i = 0
out = []
while i < questions:
    out.append(input())
    i += 1

temp = 0

i = 0
while i + 1 < len(out):
    if out[i] == out[i+1]:
        temp += 1
    i += 1

print(temp)