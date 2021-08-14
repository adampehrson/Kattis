pos = int(input())
questions = int(input())
time = 0
for x in range(questions):
    data = input().split()
    time = time + int(data[0])
    if time >= 210:
        break
    if data[1] == 'T':
        pos += 1
print(((pos-1) % 8) + 1)
