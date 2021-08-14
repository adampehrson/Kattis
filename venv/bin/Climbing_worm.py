data = list(map(int, input().split()))

climb = data[0]
fall = data[1]
top = data[2]

current = 0
amount = 0
while current < top:
    current += climb
    amount += 1
    if current >= top:
        break
    current -= fall

print(amount)