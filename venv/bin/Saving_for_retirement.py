data = list(map(int, input().split()))

bob_money = (data[1] - data[0])*data[2]

alice_money = 0
alice_age = data[3]
while alice_money <= bob_money:
    alice_money += data[4]
    alice_age += 1

print(alice_age)