prices = list(map(int, input().split()))

truck1 = list(map(int, input().split()))
truck2 = list(map(int, input().split()))
truck3 = list(map(int, input().split()))

truck1 = list(range(truck1[0], truck1[1]))
truck2 = list(range(truck2[0], truck2[1]))
truck3 = list(range(truck3[0], truck3[1]))



out = 0
for x in range(100):
    temp = 0
    if x in truck1:
        temp += 1
    if x in truck2:
        temp += 1
    if x in truck3:
        temp += 1

    if temp == 1:
        out += prices[0]
    if temp == 2:
        out += prices[1]*2
    if temp == 3:
        out += prices[2]*3

print(out)